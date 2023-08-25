# the functiond to achieve in this script:
#   a sample embeddings dataset in .csv that was indexed
#   mechanism that converted the new input into embeddings quickly
#   sentence-transformer semantic search new dataset vs. database (.cvs dataset)
#   index to pull the needed data from database to use as an input in LLM
#   give LLM the neccesary input + user live instruction, to generate best results

import openai
from environment import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY
from search.search_client import search_db
from llm.llm_agent import Conversation
from ebd.ebd import text_to_ebds_csv

# [skip if saved already] convert text in db into embeddings
text_to_ebds_csv('db/exhibit-info.csv','db/exhibit-info-ebds.csv')
text_to_ebds_csv('db/user-data.csv','db/user-data-ebds.csv')

# initiate a conversation
convo = Conversation()

while True:
    user_input = input("\nUser: ")
    # path 1: retrieve relevant information in db + user_input -> LLM
    found_db_texts = search_db(user_input, 'db/exhibit-info-ebds.csv', 'db/exhibit-info.csv')
    found_db_user_data = search_db(user_input, 'db/user-data-ebds.csv', 'db/user-data.csv')
    convo.rolling_convo(user_input, found_db_texts, found_db_user_data)
    # path 2: skip two db look-ups above todo to add if needed



# todo reduce the saved context further - summary function and remove it from the messages[] every 5 rounds for example
# todo to find a function that filter what LLM responds and stop it generate random stuff (by setting temperature to 1?)

