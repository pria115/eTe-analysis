# This file focus on the data cleaning

import os
import pandas as pd

# getting crude_suicide_rates Data
suicide_rates_data_filepath = os.path.join("raw_data", "crude_suicide_rates.csv")
suicide_rates_dataframe = pd.read_csv(suicide_rates_data_filepath)

# strip the column names
suicide_rates_dataframe = suicide_rates_dataframe.rename(columns = lambda x: x.strip())

# strip the dataframe
suicide_rates_dataframe["Country"] = suicide_rates_dataframe["Country"].str.strip()
suicide_rates_dataframe["Sex"] = suicide_rates_dataframe["Sex"].str.strip()

# save the processed data to csv file
processed_suicide_rates_data_filepath = os.path.join("processed_data", "crude_suicide_rates.csv")
suicide_rates_dataframe.to_csv(processed_suicide_rates_data_filepath)