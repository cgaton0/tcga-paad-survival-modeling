"""
Utility functions for data loading and saving.

This module provides helper functions to read and write CSV files
used throughout the TCGA-PAAD survival modeling project.
"""

import pandas as pd


def read_data(path, sep=','):
    """
    Load a CSV file into a pandas DataFrame.

    Parameters
    ----------
    path : str or Path
        Path to the CSV file.
    sep : str, optional
        Field delimiter for the CSV file (default is ',').

    Returns
    -------
    pd.DataFrame
        Loaded DataFrame.
    """

    return pd.read_csv(path, sep=sep)

def save_data(df, path):
    """
    Save a pandas DataFrame to a CSV file.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to save.
    path : str or Path
        Destination file path.

    Returns
    -------
    None
    """

    df.to_csv(path, index=False)
