from sentence_transformers import SentenceTransformer, util
import torch
import pandas as pd

# user input -> input converts into ebds
user_input = input("User: ")
ebd_model = SentenceTransformer('all-MiniLM-L6-v2') 
user_input_ebds = [ebd_model.encode(user_input)] # convert_to_tensor=True pytorch tensor containing embeddings
user_input_ebds_df = torch.FloatTensor(pd.DataFrame(user_input_ebds))

# read db embeddings as df
db_ebds_csv_path = 'db/exhibit-info-ebds.csv'
db_ebds_df = torch.FloatTensor(pd.read_csv(db_ebds_csv_path))


# ebds asymmetric semantic search against database, model: msmarco-distilroberta-base-v3
hits = util.semantic_search(user_input_ebds_df, db_ebds_df, top_k=1)
# todo question: doable to compare two DataFrame? What should be the format considering efficiency?
print(hits)

# pull database's information as text
# text + user inputs as inputs of calling LLM APIs

