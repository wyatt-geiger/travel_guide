from flask import Flask, render_template, request  # NOT the same as requests
from YouTubeAPI import youtubeAPI_request
from yelpbasic import yelp_call
from key import map_box_key

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/get_map')
def get_mapbox_map():
    yelpID = ""

    city = request.args.get('city')

    state = request.args.get('state')

    country = request.args.get('country')

    searchTerm = request.args.get('searchTerm')

    videoID = str(youtubeAPI_request(city, country))

    if searchTerm != "":
        yelpID = yelp_call(searchTerm, city, state, country)

    return render_template('mapbox_map.html', city=city, country=country, state=state, videoID=videoID,
                           yelpID=yelpID, map_box_key=map_box_key)
