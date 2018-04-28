# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:08:39 2018

@author: Kaushik
"""

import requests
import json
import time
import smtplib
import sys
import os    
from pprint import pformat
from datetime import datetime, timezone,date,timedelta
file_name =  os.path.basename(sys.argv[0])
key="X9VaaNPfOR9BFq1rtyLujDIvmF0a"

headers = { #api pull
    "Authorization": "Bearer %s" % key,
    "Content-Type": "application/json",
    "Accept": "application/json"
}
HOST = "https://api.stubhub.com"




#Sort based on Best Value
ENDPOINT1 = "/search/inventory/v2/?eventId=103233945&quantity=>2&rows=100&sort=value+desc"


url1 = "%s%s" % (HOST, ENDPOINT1)
r1 = requests.get(url1, headers=headers)
json_obj1 = r1.json()




import pandas as pd
data_value = pd.DataFrame(json_obj1['listing'])
data_value['Listing_Price'] = data_value['listingPrice'].apply(lambda x: x['amount'])
data_value['Listing_Price'] = data_value['listingPrice'].apply(lambda x: x['amount'])

#Sort based on Price
ENDPOINT2 = "/search/inventory/v2/?eventId=103233945&quantity=>2&rows=100&sort=listingPrice"
url2 = "%s%s" % (HOST, ENDPOINT2)
r2 = requests.get(url2, headers=headers)
json_obj2 =r2.json()

data_price = pd.DataFrame(json_obj2['listing'])
data_price['Listing_Price'] = data_price['listingPrice'].apply(lambda x: x['amount'])
data_price['Listing_Price'] = data_price['listingPrice'].apply(lambda x: x['amount'])


#Giants events
ENDPOINT3 = '/search/catalog/events/v3/?rows=500&q="San Francisco Giants" -PARKING&city=San Francisco'


url3 = "%s%s" % (HOST, ENDPOINT3)
r3 = requests.get(url3, headers=headers)
json_obj3 = r3.json()

data_event_giants = pd.DataFrame(json_obj3['events'])[['id','eventDateUTC','name']]

#Dodgers events
ENDPOINT4 = '/search/catalog/events/v3/?rows=500&q="Los Angeles Dodgers" -PARKING&city=Los Angeles'


url4 = "%s%s" % (HOST, ENDPOINT4)
r4 = requests.get(url4, headers=headers)
json_obj4 = r4.json()

data_event_dodgers = pd.DataFrame(json_obj4['events'])

