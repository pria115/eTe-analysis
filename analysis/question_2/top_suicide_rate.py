import os
import pandas as pd

# Getting Data
suicide_rates_data_filepath = os.path.join("raw_data", "crude_suicide_rates.csv")
suicide_rates_dataframe = pd.read_csv(suicide_rates_data_filepath)

# Filter youth data only
youth_suicide_rates_dataframe = suicide_rates_dataframe[suicide_rates_dataframe["Sex"] == " Both sexes"][["Country", " 10to19"]]

# Sorting and pick the first 5
top_five_youth_suicide_rates_dataframe = youth_suicide_rates_dataframe.sort_values(by=[' 10to19'], ascending=False).head(5)

# print the results
print(top_five_youth_suicide_rates_dataframe)