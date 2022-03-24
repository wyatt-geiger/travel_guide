from flask import Flask, render_template, request  # NOT the same as requests
from location import location_main
from YouTubeAPI import youtubeAPI_request
from yelpbasic import yelp_call
from flask_caching import Cache

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/get_map')
@cache.cached(timeout=50)
def get_mapbox_map():
    yelpID = ""

    city = request.args.get('city')

    state = request.args.get('state')

    country = request.args.get('country')

    searchTerm = request.args.get('searchTerm')

    videoID = str(youtubeAPI_request(city, country))

    if searchTerm != "":
        yelpID = yelp_call(searchTerm, city, state, country)

    return render_template('mapbox_map.html', city=city, country=country, state=state, videoID=videoID, yelpID=yelpID)
