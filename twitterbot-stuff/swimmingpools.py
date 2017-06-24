import json
import zipcode
from pprint import pprint

with open('swimmingpools.json') as data_file:    
    data = json.load(data_file)

#pprint(data)

myzip = zipcode.isequal('11102')
print myzip.state
print myzip.city.title()

print zipcode.isinradius((40.7788, -73.9227), 2.0)