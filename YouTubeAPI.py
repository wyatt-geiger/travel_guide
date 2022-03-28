import googleapiclient.discovery
import googleapiclient.errors
from location import location_main
from key import youtube_key

'''A program for sending a search request to the YouTube API'''


def youtubeAPI_request(city, state, country):
    api_service_name = "youtube"
    api_version = "v3"
    # These define which of Google's apis (YouTube) and which version of the api (v3) we are using

    youtube = googleapiclient.discovery.build(api_service_name, api_version,
                                              developerKey=get_key())
    # This line does the hard work of converting our request into a URL. It also calls to get the developerKey

    request = request_build(city, state, country, youtube)

    response = request_send(request)

    videoID = getVideoID(response)

    return videoID


def request_send(request):
    response = request.execute()
    return response


def request_build(city, state, country, youtube):
    request = youtube.search().list(
        part="snippet",  # Don't really know what this line does, but it's required
        q=subject_line(city, state, country),  # This is where the equivalent to what you'd put into the search bar
        # is put.
        type="video",
        videoCategoryId=19,  # This sets it so only videos of the YouTube category "Travel & Events" show up
        order="relevance",
        maxResults="5",  # This can be changed to give different amounts of videos per search

        # ---

        # Originally I sent YouTube location data to specify where the video should be from. However, I found I was
        # sometimes getting better results when not sending location data, as many videos didn't have location data
        # at all. Below is the remnants of that.

        # location=get_location(city, country),  # Here is where coordinates go.
        # example for formatting: 21.5922529,-158.1147114
        # locationRadius=get_radius(),  # radius around the location that will be searched for. Requires units
        # Example for formatting: 10mi

        # ----
    )

    return request


def get_key():
    key = youtube_key
    return key


def get_location(city, country):
    longitude, latitude = location_main(city, country)
    coordinates = f'{latitude},{longitude}'
    return coordinates


def get_radius():
    radius = "100mi"
    return radius


def subject_line(city, state, country):
    if state != "":
        subject = f'Things to do in {city} {state}'
        return subject
    else:
        subject = f'Things to do in {city} {country}'
        return subject


def getVideoID(youtubeData):
    y = youtubeData['items']
    return y[0]['id']['videoId']
