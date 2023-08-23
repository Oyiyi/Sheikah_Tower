import pandas as pd
import numpy as np

from sentence_transformers.util import semantic_search

# Read CSV file into a DataFrame
csv_file_path = 'db/exhibit-info-ebds.csv'
embedding_dataframe = pd.read_csv(csv_file_path, header=None)

# Convert DataFrame to a NumPy array
embedding_numpy_array = embedding_dataframe.to_numpy()

#print("NumPy Array Shape:", embedding_numpy_array.shape)
#print(embedding_numpy_array)

#hits = semantic_search(embedding_numpy_array, embedding_numpy_array, top_k=5)
#print(hits)

import numpy as np

# Given numpy array
given_array = embedding_numpy_array = embedding_dataframe.to_numpy()

# Convert the float values to strings and count the decimal places
def count_decimal_places(value):
    if '.' in value:
        return len(value.split('.')[1])
    else:
        return 0

decimal_places = max(map(count_decimal_places, map(str, given_array)))

print("Maximum Decimal Places:", decimal_places)


