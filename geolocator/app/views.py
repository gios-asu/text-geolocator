# -*- coding: utf-8 -*-
"""
Provides various URLs handles for the website
"""
from flask import render_template, request
from app import app

from nlp import LocationTagger
import geojson_maker


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def Index():
    """
    Home page of website

    URL Routes:

        * '/'
        * '/home'

    :returns: template 'index.html'
    """
    # form = OutputFormatForm()
    # if form.validate_on_submit():
    #     x = 1 / 0
    #     return UploadFile(form.geojson, form.heatmap)
        # return redirect('/index')
    return render_template(
        'index.html',
        title='Text Geolocator')


def AllowedFile(filename):
    """
    Validates file type upon upload from user

    Allowed file types:

        * .txt

    :param str filename: name of file (with extension)

    :returns: bool - True if file type is allowed; false otherwise
    """
    return '.' in filename and filename.rsplit('.', 1)[1] \
        in app.config['ALLOWED_EXTENSIONS']


@app.route('/upload', methods=['GET', 'POST'])
def UploadFile():
    """
    Receives the uploaded text of a document via POST and returns the
        geojson collection data along with a heatmap

    URL Routes:

        * '/upload'

    :returns: heatmap and pretty-printed geojson collection if file is
        uploaded via POST and is of correct file type; otherwise
        prints "No uploaded file detected"
    """
    if request.method == 'POST':
        uploadedfile = request.files['file']
        geojson = request.form.get('geojson')
        heatmap = request.form.get('heatmap')
        if uploadedfile and AllowedFile(uploadedfile.filename):

            # this is supposed to save file to /tmp/uploads
            # ---------------------------------------------------------------
            # filename = secure_filename(uploadedfile.filename)
            # uploadedfile_path =
            #     os.path.join(app.config['UPLOAD_FOLDER'],filename)
            # with open(uploadedfile_path, 'wb') as f:
            # ....f.write(uploadedfile.read())
            # return redirect(url_for('uploaded_file', filename=filename))

            text = uploadedfile.read()

            tagger = LocationTagger()
            locations = tagger.TagLocations(text)

            geojson_collection = \
                geojson_maker.MakeGeoJsonCollection(locations)

            latlngs = geojson_maker.RetrieveLatLngs(geojson_collection)

            return render_template(
                'result.html',
                latlngs=latlngs,
                center=latlngs[0],
                heatmap=str(heatmap),
                geojson=str(geojson),
                geojson_collection=geojson_collection
            )
    return '''<!doctype html><title>Upload new File</title><body>
           <p>No uploaded file detected.</p></body>'''
