from sentence_transformers import SentenceTransformer, util
import torch
import pandas as pd
import numpy as np

def search_db(user_input, db_ebds_csv_path, db_text_csv_path): # todo add path here so that it can search diff db
    # data prep for search function: read db embeddings as np
    db_ebds_csv_path = db_ebds_csv_path
    db_ebds_np = torch.FloatTensor(pd.read_csv(db_ebds_csv_path, header=None).to_numpy())

    # data prep for search function: user input converts into ebds
    ebd_model = SentenceTransformer('all-MiniLM-L6-v2') 
    user_input_ebds_np = torch.FloatTensor(ebd_model.encode(user_input)) # np class as output object. todo to try for speed: convert_to_tensor=True pytorch tensor containing embeddings

    # ebds semantic search against database
    # todo model is not accurate. Possible reasons 1) two many sentences; 2) wrong model? -> to update into asymmetric model: msmarco-distilroberta-base-v3. Seems like not authorized?
    hits = util.semantic_search(user_input_ebds_np, db_ebds_np, top_k=2) # todo cos score > xxx?
    # search

    # pull database's information as text
    db_texts_csv_path = db_text_csv_path
    db_texts = pd.read_csv(db_texts_csv_path, header=None, encoding='iso-8859-1')
    found_db_texts = db_texts.iloc[[hits[0][i]['corpus_id'] for i in range(len(hits[0]))]]
    return found_db_texts