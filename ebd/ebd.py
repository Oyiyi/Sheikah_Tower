# todo to make a function so that to call this function for both database and user search
import pandas as pd
from sentence_transformers import SentenceTransformer

# settings: define which model to use. Size 384 for each sentence.
ebd_model = SentenceTransformer('all-MiniLM-L6-v2') 

# todo to bring true inputs
#Our sentences we like to encode
sentences = ['This framework generates embeddings for each input sentence',
    'Sentences are passed as a list of string.',
    'The quick brown fox jumps over the lazy dog.']

#Sentences are encoded by calling model.encode()
ebds = ebd_model.encode(sentences)

#Print the embeddings
for sentence, ebd in zip(sentences, ebds): # zip combines nth and nth
    print("Sentence:", sentence)
    print("Embedding:", ebd)
    print("")

# ebd into dataframe (n rows for each sentences x 384 each) (3 rows x 384 columns)
ebds = pd.DataFrame(ebds)
print(ebds)

# todo how to connect multi index 1. searched index from semantic search; 2. gallery-exhibit manual index