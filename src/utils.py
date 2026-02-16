import pandas as pd
import numpy as np


def read_data(path, sep=','):
    """ Recibe un path y un separador y devuelve un dataframe. """

    return pd.read_csv(path, sep=sep)
    

def save_data(df, path):
    """ Recibe un dataframe y un path y guarda el dataframe en un archivo csv.
    """

    df.to_csv(path, index=False)