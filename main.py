""" 
Steps:
  a sample embeddings dataset in .csv that was indexed
  mechanism that converted the new input into embeddings quickly
  sentence-transformer semantic search new dataset vs. database (.cvs dataset)
  index to pull the needed data from database to use as an input in LLM
  give LLM the neccesary input + user live instruction, to generate best results
"""

import openai
from environment import OPENAI_API_KEY
from datetime import datetime
openai.api_key = OPENAI_API_KEY
from search.search_client import search_db
from llm.llm_agent import Conversation
from ebd.ebd import text_to_ebds_csv
from mec_apis.location_manager import LocationManager

# [skip if saved already] convert text in db into embeddings
#text_to_ebds_csv('db/exhibit-info.csv','db/exhibit-info-ebds.csv')
#text_to_ebds_csv('db/user-data.csv','db/user-data-ebds.csv')

# initiate a conversation
convo = Conversation()

# initatie a location manager
log_file_path = "db/user_event_log_file.json"
db_location_file_path = "db/monaco_coordinates.json"
user_IP_address = '10.100.0.4'
locationManager = LocationManager(user_IP_address, log_file_path, db_location_file_path)
event = locationManager.fetch_nearby_locations()

def loc_api():
    # @Qi live information to present by UI
    user_live_coor = f"User now at: {event['user_live_coor']}"
    nearby_locations = f"{list(event.keys())[2]}: {event[list(event.keys())[2]]}" # 3rd key is 'nearby_locations within 500'
    # check to delete
    print(user_live_coor)
    print(nearby_locations)
    return user_live_coor, nearby_locations

def chat_api(user_input):
    found_db_texts = search_db(user_input, 'db/exhibit-info-ebds.csv', 'db/exhibit-info.csv')
    print(found_db_texts)
    found_db_user_data = search_db(user_input, 'db/user-data-ebds.csv', 'db/user-data.csv')
    print(found_db_user_data)
    output = convo.rolling_convo(user_input, found_db_texts, found_db_user_data)
    return output

if __name__ == '__main__':

  while True:
      user_input = input("\n\nUser: ")
      output = chat_api(user_input)
      print(output)


# todo reduce the saved context further - summary function and remove it from the messages[] every 5 rounds for example
# todo to find a function that filter what LLM responds and stop it generate random stuff (by setting temperature to 1?)

