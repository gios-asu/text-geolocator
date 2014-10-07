text-geolocator
===============

Fall 2014/Spring 2015 CS Capstone - Generating heatmaps from and searching for geolocation data from text documents

## Install Instructions
- Install docker. http://docker.com Follow the directions provided for the target system.
- Install Python. (If it hasn't been already)
- Install pip.
- Install fig with `sudo pip install -U fig`
- Clone the repo. `git clone https://github.com/gios-asu/text-geolocator.git`
- Start the docker containers and development environment. `sudo fig up -d`
- Verify that everything started up ok. `sudo fig ps`

## Example request and response

HTTP Request
```
POST /geocode
Content: "This article is about the Dinagat Islands, in the middle of some large region." 
```

RESPONSE (in [geojson](http://geojson.org/)):
```javascript
[{
  "type": "Feature",
  "properties": {
    "weight": 1.0,
    "name": "Dinagat Islands"
    },
  "geometry": {
    "type": "Point",
    "coordinates": [125.6, 10.1]
  }
}, {
    "type": "Feature",
    "properties": {
      "weight": 0.5,
      "name": "some large region"
      },
    "geometry": {
        "type": "Polygon",
        "coordinates": [[
            [-109.05, 41.00],
            [-102.06, 40.99],
            [-102.03, 36.99],
            [-109.04, 36.99],
            [-109.05, 41.00]
        ]]
    }
}]
```
