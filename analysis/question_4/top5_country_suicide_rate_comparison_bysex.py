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
print(suicide_rate_dataframe.head())


# Do Melting - Tranform/Combine the multiple  column names of different age groups into one column "Age"
suicide_rate_pivot_longer_df = pd.melt(suicide_rate_dataframe, id_vars=['Country', 'Sex'], value_vars=['80_above','70to79', '40to49', '30to39', '20to29', '10to19', 'all_age'], var_name='Age',value_name='Suicide_rate')
print(suicide_rate_pivot_longer_df)


#
# Find Top 5 countries of highest suicide rate in 'all_age' and "both sexes"
# And Male/ Female - Age distribution 
top_10_suicide_rate_bothsex = suicide_rate_pivot_longer_df[(suicide_rate_pivot_longer_df['Sex'] == 'Both sexes' ) & (suicide_rate_pivot_longer_df['Age'] == 'all_age' )].nlargest(5, 'Suicide_rate')
suicide_rate_separatesex = suicide_rate_pivot_longer_df[suicide_rate_pivot_longer_df['Sex'] != 'Both sexes']

## Get the countries names
print(top_10_suicide_rate_bothsex['Country'].to_list())
top_10_country_names = top_10_suicide_rate_bothsex['Country'].to_list()
final = suicide_rate_separatesex[suicide_rate_separatesex['Country'].isin(top_10_country_names)]

print("final......",final.head())


sns.set_style("whitegrid")
gg = sns.catplot(data = final, kind="bar", x="Country", y="Suicide_rate",hue="Sex", palette="husl", alpha=.9, height=5)
gg.despine(top=False).set_ylabels("Suicide rate")
plt.title("Top 5 Countries with Highest Suicide Rate")
plt.show()