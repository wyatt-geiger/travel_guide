import csv
import ast
from flask import Flask, render_template, request, redirect
from YouTubeAPI import youtubeAPI_request
from yelpbasic import yelp_call
import bookmark_schema
from flask_caching import Cache
from key import map_box_key
from datetime import datetime
from datetime import timedelta

config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/get_map', methods=['GET'])
@cache.cached(timeout=50)
def get_mapbox_map():
    try:
        city = request.args.get('city')

        state = request.args.get('state')

        if state is None:
            state = ""

        country = request.args.get('country')

        searchTerm = request.args.get('searchTerm')

        try:  # This will test to see if a file containing cache data already exists
            cache_data = open('cache_data.csv')
            cache_reader = csv.reader(cache_data)
            clean_cache()  # Calls the function that will clean the catch of any old entries
            for row in cache_reader:
                if row:  # Prevents the program from crashing when encountering a blank line
                    # this loop tests if the city, state, and country inputted by the user match any entries in the cache
                    if city + state + country == row[0] + row[1] + row[2]:
                        videoID = row[4]  # If a match is found, the youtube video from the cache is saved

                        if searchTerm == row[3] and searchTerm != '':
                            # if the search term also matches, (and isn't blank) then the cached yelp data is also saved
                            yelpID = ast.literal_eval(row[5])
                            # learned of ast from here: https://www.askpython.com/python/string/python-convert-string-to-list
                            # The yelp data is saved as a list, within a csv file.
                            # This is weird, and requires a weird solution (This ast thing) to make the list readable again.

            cache_data.close()
        except FileNotFoundError:
            print("File not found")
            # If the csv file doesn't exist, it will be made later

        try:  # code idea from https://www.oreilly.com/library/view/python-cookbook/0596001673/ch17s02.html
            videoID
        except NameError:
            videoID = None
        if videoID is None:
            videoID = str(youtubeAPI_request(city, state, country))
        # If the csv file doesn't exist, or there isn't cached data for this search, then videoID won't exist.
        # This tests if videoID was saved from cache or not. If not, is calls the API to make videoID.
        # The same process happens below with the yelpID
        try:
            yelpID
        except NameError:
            yelpID = ''
        if yelpID == '' and searchTerm != "":
            yelpID = yelp_call(searchTerm, city, state, country)

        # Below handles the creation/modification of the cache csv file.
        cache_data = open('cache_data.csv', 'a', newline='')
        cache_writer = csv.writer(cache_data)
        cache_writer.writerow([city, state, country, searchTerm, videoID, yelpID, datetime.now()])
        cache_data.close()

        return render_template('mapbox_map.html', city=city, country=country, state=state, yelpID=yelpID,
                               searchTerm=searchTerm, map_box_key=map_box_key, videoID=videoID)
    except:
        return render_template('search_error.html')

@app.route('/get_map', methods=['POST'])
def submit_post():
    name = request.form.get('name')
    rating = request.form.get('rating')
    address = request.form.get('address')
    business_city = request.form.get('city')
    telephone = request.form.get('telephone')

    bookmark_schema.insert_data(name, rating, address, business_city, telephone)

    return redirect(request.referrer)


@app.route('/get_bookmarks', methods=['GET', 'POST'])
def bookmark_page():

    try:
        if request.method == 'POST':
            name = request.form.get('name')
            bookmark_schema.delete_data(name)
            return redirect('/get_bookmarks')   # reload the bookmarks page, by default a get request. now without the deleted item

        else:
            bookmark_data = bookmark_schema.display_all_data()
            return render_template('bookmark.html', bookmark_data=bookmark_data)
    except:
        return render_template('search_error.html')

def clean_cache():  # Function that deletes old data from the cache
    cleaned_cache = []
    delete_date = datetime.now() - timedelta(days=1)  # Looks for entries that are one day old or older
    with open('cache_data.csv', 'r', newline='') as cache_data:  # Goes through the cache. Makes a list of good entries
        cache_reader = csv.reader(cache_data)
        for row in cache_reader:
            if row:  # Prevents the program from crashing when encountering a blank line
                previousTime = datetime.strptime(row[6], "%Y-%m-%d %H:%M:%S.%f")
                # Code for converting the saved datetime back into a datetime object:
                # https://stackoverflow.com/questions/13356632/converting-a-datetime-into-a-string-and-back-again
                if previousTime >= delete_date:
                    cleaned_cache.append(row)
    with open('cache_data.csv', 'w', newline='') as cache_data:  # Clears cache before adding the good entries back in
        cache_writer = csv.writer(cache_data)
        cache_writer.writerows(cleaned_cache)
        