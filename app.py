from flask import Flask, render_template, request  # NOT the same as requests
from location import get_location

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/get_map')
def get_mapbox_map():

    city = request.args.get('city')
    
    country = request.args.get('country')

    return render_template('mapbox_map.html', city=city, country=country)

