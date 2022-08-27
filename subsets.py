import numpy as np
import pandas as pd

# importing the raw data into pandas dataframe
master_data = pd.read_csv("olympics_medals_country_wise.csv")

# removing whitespaces from column names
master_data.columns = master_data.columns.str.replace(' ', '')

# replacing empty "region" cells with NaN
master_data['region'].replace('', np.nan, inplace=True)

# droppin the rows with NaN for region and resetting index
master_data = master_data.dropna(subset=['region'])
master_data = master_data.reset_index(drop=True)

# subsetting data by regions and index reset
asia = master_data[master_data['region'] == 'Asia']
asia = asia.reset_index(drop=True)

africa = master_data[master_data['region'] == 'Africa']
africa = africa.reset_index(drop=True)

middle_east = master_data[master_data['region'] == 'Middle East']
middle_east = middle_east.reset_index(drop=True)

south_america = master_data[master_data['region'] == 'South America']
south_america = south_america.reset_index(drop=True)

north_america = master_data[master_data['region'] == 'North America']
north_america = north_america.reset_index(drop=True)

central_america = master_data[master_data['region'] == 'Central America']
central_america = central_america.reset_index(drop=True)

europe = master_data[master_data['region'] == 'Europe']
europe = europe.reset_index(drop=True)

oceania = master_data[master_data['region'] == 'Oceania']
oceania = oceania.reset_index(drop=True)

