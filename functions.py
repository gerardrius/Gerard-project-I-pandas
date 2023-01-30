# Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# Datasets
attacks = attacks = pd.read_csv("attacks.csv", index_col=0, encoding='latin-1')

# Generic Cleaning
def column_remover(df, drop_columns_list):
    df.drop(drop_columns_list, axis = 1, inplace = True)
    return df
    
def drop_dupl (df):
    df.drop_duplicates(inplace=True)
    return df

def drop_all_nans (df):
    return df.dropna(how="all", axis=0, inplace=True)

def drop_any (df):
    df.dropna(how="any", axis=0, inplace=True)
    return df

def filter_by_pattern(df, column, pattern):
    mask = df[column].str.contains(pattern, na=False, regex=True)
    df = df[mask]
    return df

def month_number(x):
    months = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr':4,
        'May':5,
        'Jun':6,
        'Jul':7,
        'Aug':8,
        'Sep':9,
        'Oct':10,
        'Nov':11,
        'Dec':12
    }
    try:
        x = months[x]
        return x
    except KeyError:
        pass

def weekdays (df):
    weekdays_list = []
    for i in range(df.shape[0]): 
        try:
            weekday = datetime.date(attacks["Year"][i], int(attacks["Month"][i]), attacks["Day"][i]).strftime('%w')
            weekdays_list.append(weekday)
        except ValueError:
            weekdays_list.append(np.nan)

    df["Weekday"] = weekdays_list    
        
# Analysis
    # Get list with all variables in the dataframe
def variables_list (df):
   variables =  list(df.keys())
   return variables

    # Duplicates count
def duplicates (df):
    duplicated_rows = df.duplicated().sum()
    print(f"Sharks' dataset contains {duplicated_rows} duplicated rows out of {df.shape[0]}.")

    # Get sample
def df_sample (df, num):
    return df.sample(num)

    # Different datatypes for each variable
def df_datatypes (df):
    variables_datatypes = {}

    for variable in df.keys():
        variables_datatypes[variable] = set()
    
        for i in range(0, df.shape[0]):
            variables_datatypes[variable].add(type(df[variable][i]).__name__)

    for key, values in variables_datatypes.items():
        if len(values) == 1:
            print(f"{key} only has one data type: {values}.")
        else:
            print(f"{key} has {len(values)} data types: {values}.")
    
    return variables_datatypes

# Visualizations
plt.style.use("classic")
sns.set(rc={"figure.figsize":(12,6)})