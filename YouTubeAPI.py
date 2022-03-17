import googleapiclient.discovery
import googleapiclient.errors

'''A program for sending a search request to the YouTube API'''

def main():
    api_service_name = "youtube"
    api_version = "v3"
    # These define which of google's apis (YouTube) and which version of the api (v3) we are using

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=get_key())
    # This line does the hard work of converting our request into a URL. It also calls to get the developerKey

    request = youtube.search().list(  # Here the YouTube search request in necessary
        part="snippet",  # Don't really know what this line does, but it's required
        location=get_location(),  # Here is where coordinates go. example for formatting: 21.5922529,-158.1147114
        locationRadius=get_radius(),  # radius around the location that will be searched for. Requires units
        # Example for formatting: 10mi
        q=subject_line(),  # This is where the equivalent to what you'd put into the search bar is put.
        type="video",
        maxResults="5",  # This can be changed to give different amounts of videos per search
    )
    response = request.execute()

    print(response)

def get_key():
    key = input('Paste your API key here: ')
    return key

def get_location():
    coordinates = input('Paste coordinates here: ')
    return coordinates

def get_radius():
    radius = input('Type radius: ')
    return radius

def subject_line():
    subject = input('Type subject: ')
    return subject

if __name__ == "__main__":
    main()
