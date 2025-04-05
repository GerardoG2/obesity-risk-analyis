"""
Functions for loading datasets as a dataframe.
Each function contains the datasource and a brief description of the data. 
"""
import pandas as pd

def load_uci_obesity_data(file_path = "DataSets/UCI_ObesityDataSet"):
    """
    Load UCI dataset as dataframe.

    Title: "Estimation of Obesity Levels Based On Eating Habits and Physical Condition"

    Key features: gender, age, height, weight, eating habits, physical conditon, lifestyle habits

    Source: https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition
    """
    return pd.read_csv(file_path)

def load_cdc_obesity_data(file_path = "DataSets/CDC_ObesityDataSet"):
    """
    Load CDC dataset as dataframe.

    Title: "Normal weight, overweight, and obesity amond adults aged 20 and over,
    by selected characteristics: United States"

    Key features: BMI, sex, age, obesity by sex, obesity by poverty level, categorization of obesity levels,

    Source: https://data.cdc.gov/NCHS/Normal-weight-overweight-and-obesity-among-adults-/3nzu-udr9
    """
    return pd.read_csv(file_path)