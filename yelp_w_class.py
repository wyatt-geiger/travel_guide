import requests
from pprint import pprint

from key import my_key


class Yelp:
        #this is the method that is called when the instance of Yelp is created
        def __init__(self,u='',h='',p=''):
                self.headers=h
                self.parameter=p
                self.url=u
                self.business_data={}
        # this method is to initialize the variables like headers,parameters and url 
        def readData(self):
                                
                API_key = my_key
                self.url = 'https://api.yelp.com/v3/businesses/search'
                self.headers = {
                        'Authorization': 'Bearer %s' % API_key,
                }
                term=input("Input The Term to Search Yelp : ")
                location=input("Input The Location to Search Yelp : ")
                radius =int(input("Input The Radius Value : "))
                limit = int(input("Input the Limit of restraunts: "))
                self.parameter = {
                        'term': term,
                        'location': location,
                        'radius': radius,
                        'limit': limit    
                        }
        # this method is called to process get request with the paramets read in readData()
        def process(self):
                response = requests.get(url = self.url, params = self.parameter, headers=self.headers)
                #convert the json string to dic
                self.business_data = response.json()
                # print(business_data.keys()) # to see the dictionary for the of all [businnes, total, region]

                
        # this method is display the data fetched in the process() method 
        def showBusinessData(self):
                if len(self.business_data)==0:
                        print("NO DATA FOUND")
                # else:
               
               
                for businen_names in self.business_data["businesses"]:  # show only the business  
                
                        print("{:35s}{:5.2f}{:>25s}{:>25s}".format(businen_names['name'],
                        
                        businen_names['location']['address1'],
                        businen_names['location']['city'],
                        businen_names['phone'],
                        businen_names['rating'],
                        businen_names['review_count'],
                        businen_names['coordinates']['latitude']
                        ))
        
                # print('SOME ERROR OCCURED ')


y=Yelp()
y.readData()
y.process()
y.showBusinessData()

