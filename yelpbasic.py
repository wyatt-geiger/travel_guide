import requests
from pprint import pprint

from key import yelp_key


def yelp_call(search_term, city, state, country):
    API_key = yelp_key

    url = 'https://api.yelp.com/v3/businesses/search'

    headers = {
        'Authorization': 'Bearer %s' % API_key,
    }

    term = search_term
    if state == "":
        location = city
    else:
        location = city
    radius = 16090
    limit = 5

    Parameter = {
        'term': term,
        'location': location,
        'radius': radius,
        'limit': limit

    }

    response = requests.get(url=url, params=Parameter, headers=headers, )

    # convert the json string to dic
    business_data = response.json()
    business_list = yelp_interpreter(business_data)
    return business_list
    # print(business_data.keys()) # to see the dictionary for the of all [businnes, total, region]


def yelp_interpreter(business_data):
    business_list = []
    for business_names in business_data["businesses"]:
        business_list.append([business_names['name'],
                              business_names['rating'],
                              business_names['location']['address1'],
                              business_names['location']['city'],
                              business_names['phone']])
        # print("{:25s}{:5.2f}{:>25s}{:>25s}{:>15}{:>25}{:>15f}".format(business_names['name'],
        #                                                               business_names['rating'],
        #                                                               business_names['location']['address1'],
        #                                                               business_names['location']['city'],
        #                                                               business_names['phone'],
        #                                                               business_names['review_count'],
        #                                                               business_names['coordinates']['latitude']
        #                                                               ))
    return business_list

#
# for businen_names in business_data["businesses"]:  # show only the business names
#     # print(businen_names['name'])  #show only the business names s
#     print("{:25s}{:5.2f}{:>25s}{:>25s}{:>15}{:>25}{:>15f}".format(business_names['name'],
#                                                                   business_names['rating'],
#                                                                   business_names['location']['address1'],
#                                                                   business_names['location']['city'],
#                                                                   business_names['phone'],
#                                                                   business_names['review_count'],
#                                                                   business_names['coordinates']['latitude']
#                                                                   ))