# This code is the analysis on the top 5 countries with hight suicide rates
# It further attempts to explore their differences and similarity of suicide rates in different age groups
# barplot from Seaborn library is used for visualisation 

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Getting Data of crude suicide rate
suicide_rate_data_filepath = os.path.join("..","processed_data", "crude_suicide_rates.csv")
suicide_rate_dataframe = pd.read_csv(suicide_rate_data_filepath, index_col=0)
#print(human_resource_dataframe.head())


# Calculate the total suicide rate of all different ages
suicide_rate_dataframe['all_age'] = suicide_rate_dataframe['80_above']+ suicide_rate_dataframe['70to79'] + suicide_rate_dataframe['60to69']+ suicide_rate_dataframe['50to59']
+ suicide_rate_dataframe['40to49']+ suicide_rate_dataframe['30to39']+ suicide_rate_dataframe['20to29'] + suicide_rate_dataframe['10to19']
#print(suicide_rate_dataframe.head())


# Find Top 5 countries of highest suicide rate in 'all_age' and "both sexes"
top_5_suicide_rate = suicide_rate_dataframe[suicide_rate_dataframe['Sex'] == 'Both sexes'].nlargest(5, 'all_age')
#print(top_5_suicide_rate.head())

# Do Melting - Tranform/Combine the multiple  column names of different age groups into one column "Age"
top_5_suicide_rate_pivot_longer_df = pd.melt(top_5_suicide_rate, id_vars=['Country'], value_vars=['80_above','70to79', '40to49', '30to39', '20to29', '10to19'], var_name='Age',value_name='Suicide_rate')
#print(top_5_suicide_rate_pivot_longer_df)


# Plotting the result
sns.set(color_codes=True)
plot_top5_country = sns.barplot(x='Country', y='Suicide_rate', hue='Age', data = top_5_suicide_rate_pivot_longer_df)
plt.title("Top 5 Countries with Highest Suicide Rate")
plt.ylabel("Suicide rate per 100,000 population")
plt.show()