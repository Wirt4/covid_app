from flask import Flask
from geolocator import GeoLocator
app = Flask(__name__)
@app.route('/')
def hello_world():
    gl = GeoLocator
    #returns the current county we're in
    county = gl.county_no_parameters(gl)[1]
    return f"Hello, your IP address is in {county}"
