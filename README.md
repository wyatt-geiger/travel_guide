API keys can be found at these links:

YouTube API: https://console.cloud.google.com/apis/credentials (Have YouTube account, Create project, then create credentials)
Map Box API: https://account.mapbox.com/access-tokens/create
Yelp API: https://www.yelp.com/developers/documentation/v3/authentication

Edit key.py and add your keys to the spaces provided


This program is intended to be used as a travel guide. The user can enter a city, state (if in the United States), country,
and a search term for looking up businesses in the area (optional parameter). From there, the user will be directed to a new
page which contains information about the place they looked for. Information includes a map (from mapbox API), a YouTube video
that gives travel information (YouTube API), and business information for the businesses they searched for (Yelp API).

Using the business information provided by the Yelp API, the user can bookmark businesses into a database, which can be viewed
on the bookmarks page. The bookmarks page reads the database so the user can view their current bookmarks. Users can also choose
to delete bookmarks. The program utilizes a cache feature so that when the user clicks the "Back" button on the bookmarks page,
they are taken back to the result they previously entered. After 50 seconds, the cache expires and the user would have to return
to the main page.

To catch invalid user input, as well as the expired cache, a generic error page is displayed informing the user of the error
and allowing them to return to the main page.
