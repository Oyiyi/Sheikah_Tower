"""
location API manager
Main Zone for demo:zone02 (many options for historical tourism spots, food, mesuems) 
Demo for communication across zones (hospital in zone01)

Step 1: once user initiate the conversation, retrieve live location. Refresh every [1] min (or area enter subscription), saved in json file as log events data
Step 2: retrieve the surrounding locations within [5] meters of user coordinates, saved in [?] a list nearby_locations_list
Step 3: based on the goal of the conversation / chat history, gather {data} from these locations, saved in [?].
Step 4: use the {data} to generate LLM response / translation
Step 5: fine-tuning model locally every 24 hours
"""

import requests, time, math, json
from mec_location_api import fetch_user_coordinates, distance_calc


class LocationReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.locations = self._read_locations()

# read the locations and their coordinates from the db
locations_file_path = "monaco_coordinates.json" # db path
with open(locations_file_path, 'r') as json_file:
    locations = json.load(json_file)

#user_IP_address = '10.100.0.4'

def fetch_nearby_locations(user_IP_address):
	#while True: # todo to update into if a conversation initiated by user
	user_live_coor = fetch_user_coordinates(user_IP_address) # todo to save it in a log event file - LowP

	for location, coordinates in locations.items(): # key, values
		distance = distance_calc(user_live_coor[0], user_live_coor[1], coordinates["latitude"], coordinates["longitude"])
		if distance < 100 # to define
			nearby_locations_list = [] # todo think where to make it [] again
			nearby_locations_list.append(location)
			prompt_nearby_locations = f"Now user is close to: {', '.join(nearby_locations_list)}"

	return prompt_nearby_locations
	#time.sleep(2) # in second; todo maybe to refresh every 2 second. Now refresh the nearby location by response
	# todo interestRealm. Thinking about the data saved under the zone - access point. Maybe shorten the list into one zone so that the calculation is easier