# the function to achieve in this script: a sample embeddings dataset in .csv that was indexed
# mechanism that converted the new input into embeddings quickly
# sentence-transformer semantic search new dataset vs. database (.cvs dataset)
# index to pull the needed data from database to use as an input in LLM
# give LLM the neccesary input + user live instruction, to generate best results

#
import openai
from environment import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY


#from ebd import ebd
from llm.llm_agent import Conversation

# 1 - To initiate a conversation
convo = Conversation()
convo.start_rock()

# todo issue: successfully called, but can't continue the conversation
'''
raise self.handle_error_response(openai.error.InvalidRequestError: 'AI' is not one of ['system', 'assistant', 'user', 'function'] - 'messages.2.role'
'''



