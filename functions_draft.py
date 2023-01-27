# Libraries
import pandas as pd
import numpy as np

# Datasets
attacks = attacks = pd.read_csv("attacks.csv", index_col=0, encoding='latin-1')

# Cleaning
def column_remover(dataframe, drop_columns_list):
    dataframe.drop(drop_columns_list, axis = 1, inplace = True)
    return dataframe
    

# Analysis
def variables_list (df):
   variables =  list(df.keys())
   return variables

# Visualizations

