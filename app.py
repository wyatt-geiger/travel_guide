from flask import Flask, render_template, request  # NOT the same as requests
from location import location_main
from YouTubeAPI import youtubeAPI_request
import bookmark_schema
## from yelpbasic import business_data

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/get_map')
def get_mapbox_map():

    city = request.args.get('city')
    
    state = request.args.get('state')

    country = request.args.get('country')

    videoID = str(youtubeAPI_request(city, country))
    
    ## yelpID =  str(business_data)


   

    return render_template('mapbox_map.html', city=city, country=country, state=state, videoID=videoID)
## , yelpID = yelpID

@app.route('/get_bookmarks')
def bookmark_page():

    bookmark_schema.create_table()

    bookmark_data = bookmark_schema.display_all_data()

    return render_template('bookmark.html', bookmark_data=bookmark_data)
