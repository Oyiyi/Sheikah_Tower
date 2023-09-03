import openai
from environment import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY
from search.search_client import search_db
from llm.llm_agent import Conversation
from ebd.ebd import text_to_ebds_csv

# [skip if saved already] convert text in db into embeddings
#text_to_ebds_csv('db/exhibit-info.csv','db/exhibit-info-ebds.csv')
#text_to_ebds_csv('db/user-data.csv','db/user-data-ebds.csv')

class ChatApi():
    def __init__(self) -> None:
        self.convo = Conversation()

    def chat_api(self, user_input):
        found_db_texts = search_db(user_input, 'db/exhibit-info-ebds.csv', 'db/exhibit-info.csv')
        found_db_user_data = search_db(user_input, 'db/user-data-ebds.csv', 'db/user-data.csv')
        
        output = self.convo.rolling_convo(user_input, found_db_texts, found_db_user_data)
        return output


