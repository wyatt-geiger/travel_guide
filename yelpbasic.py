
import requests
from pprint import pprint

from key import my_key



API_key = my_key

url = 'https://api.yelp.com/v3/businesses/search'

headers = {
        'Authorization': 'Bearer %s' % API_key,
    }



term=input("Input The Term to Search Yelp : ")
location=input("Input The Location to Search Yelp : ")
radius =int(input("Input The Radius Value : "))
limit = int(input("Input the Limit of restraunts: "))

Parameter = {
        'term': term,
        'location': location,
        'radius': radius,
        'limit': limit
       
        }


response = requests.get(url = url, params = Parameter, headers=headers, )

#convert the json string to dic
business_data = response.json()
# print(business_data.keys()) # to see the dictionary for the of all [businnes, total, region]


for businen_names in business_data["businesses"]:  # show only the business names 
        # print(businen_names['name'])  #show only the business names s
        print("{:25s}{:5.2f}{:>25s}{:>25s}{:>15}{:>25}{:>15f}".format(businen_names['name'],businen_names['rating'],businen_names['location']['address1'],
        businen_names['location']['city'],businen_names['phone'],businen_names['review_count'],businen_names['coordinates']['latitude']
        ))
        



       
