
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import logging

warnings.filterwarnings(action="ignore")

logging.basicConfig(
    level=logging.INFO,
    filename="model.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

# Step 1: Data Ingestion

def data_ingestion():
    """
    *Title: composite cement strength prediction model

    *Shape of dataset: (1030, 10)

    *Dataset: Concrete_Data.csv

    *Independent columns:
    Cement (component 1)(kg in a m^3 mixture)
    Blast Furnace Slag (component 2)(kg in a m^3 mixture)
    Fly Ash (component 3)(kg in a m^3 mixture)
    Water (component 4)(kg in a m^3 mixture)
    Superplasticizer (component 5)(kg in a m^3 mixture)
    Coarse Aggregate (component 6)(kg in a m^3 mixture)
    Fine Aggregate (component 7)(kg in a m^3 mixture)
    Age (day)

    *Target column:
    Concrete compressive strength(MPa, megapascals)
    """

    df = pd.read_csv("C:\composite-cement-strength-prediction-model\data\Concrete_Data - Concrete_Data.csv")

    return df
