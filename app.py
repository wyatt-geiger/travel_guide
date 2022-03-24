from tabnanny import check
from flask import Flask, render_template, request, redirect
from location import location_main
from YouTubeAPI import youtubeAPI_request
from yelpbasic import yelp_call
import bookmark_schema

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/get_map', methods=['GET', 'POST'])
def get_mapbox_map():

    if request.method == 'GET':

        city = request.args.get('city')

        state = request.args.get('state')

        country = request.args.get('country')

        searchTerm = request.args.get('searchTerm')

        videoID = str(youtubeAPI_request(city, country))

        if searchTerm != "":
            yelpID = yelp_call(searchTerm, city, state, country)
        
        return render_template('mapbox_map.html', city=city, country=country, state=state, videoID=videoID, yelpID=yelpID)
    
    else:
        name = request.form.get('name')
        rating = request.form.get('rating')
        address = request.form.get('address')
        business_city = request.form.get('city')
        telephone = request.form.get('telephone')

        bookmark_schema.insert_data(name, rating, address, business_city, telephone)
  
        return redirect(request.referrer)

@app.route('/get_bookmarks', methods=['GET', 'POST'])
def bookmark_page():

    if request.method == 'POST':
        name = request.form.get('name')
        bookmark_schema.delete_data(name)
        return redirect('/get_bookmarks')   # reload the bookmarks page, by default a get request. now without the deleted item
        # todo error handling 

    else:

        bookmark_data = bookmark_schema.display_all_data()
        return render_template('bookmark.html', bookmark_data=bookmark_data)
