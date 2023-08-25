# todo to make a function so that to call this function for both database and user search
import pandas as pd
from sentence_transformers import SentenceTransformer

# settings: define which model to use. Size 384 for each sentence.
ebd_model = SentenceTransformer('all-MiniLM-L6-v2') 

'db/exhibit-info.csv'
'db/exhibit-info-ebds.csv'

def text_to_ebds_csv(db_input_csv_path, db_output_csv_path):
    # convert data in database into embeddings, save to output.csv
    db_texts_csv_path = db_input_csv_path
    db_ebds_csv_path = db_output_csv_path
    db_texts = pd.read_csv(db_texts_csv_path, header=None, squeeze=True, encoding='iso-8859-1')
    db_ebds = [ebd_model.encode(i) for i in db_texts] # encode()->class 'numpy.ndarray'.convert_to_tensor=True pytorch tensor containing embeddings
    db_ebds_df = pd.DataFrame(db_ebds)
    db_ebds_df.to_csv(db_ebds_csv_path, index=False, header=False, float_format='%.20f')
    print(f"\n\n...texts in database ({db_input_csv_path}) were embedded and saved successfully.")