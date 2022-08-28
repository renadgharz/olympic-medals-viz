import numpy as np
import pandas as pd

# importing the raw data into pandas dataframe
master_data = pd.read_csv("data/olympics_medals_country_wise.csv")

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

asia.to_csv("data/asia.csv", index=True)


africa = master_data[master_data['region'] == 'Africa']
africa = africa.reset_index(drop=True)

africa.to_csv("data/africa.csv", index=True)


middle_east = master_data[master_data['region'] == 'Middle East']
middle_east = middle_east.reset_index(drop=True)

middle_east.to_csv("data/middle_east.csv", index=True)


south_america = master_data[master_data['region'] == 'South America']
south_america = south_america.reset_index(drop=True)

south_america.to_csv("data/south_america.csv", index=True)


north_america = master_data[master_data['region'] == 'North America']
north_america = north_america.reset_index(drop=True)

north_america.to_csv("data/north_america.csv", index=True)


central_america = master_data[master_data['region'] == 'Central America']
central_america = central_america.reset_index(drop=True)

central_america.to_csv("data/central_america.csv", index=True)


europe = master_data[master_data['region'] == 'Europe']
europe = europe.reset_index(drop=True)

europe.to_csv("data/europe.csv", index=True)


oceania = master_data[master_data['region'] == 'Oceania']
oceania = oceania.reset_index(drop=True)

oceania.to_csv("data/oceania.csv", index=True)


# subsetting for summer competitions only
summer_asia = asia[['countries', 'summer_participations', 'summer_gold', 'summer_silver', 'summer_bronze',
                    'summer_total']]

summer_asia.to_csv("data/summer_asia.csv", index=True)


summer_africa = africa[['countries', 'summer_participations', 'summer_gold', 'summer_silver', 'summer_bronze',
                        'summer_total']]

summer_africa.to_csv("data/summer_africa.csv", index=True)


summer_middle_east = middle_east[['countries', 'summer_participations', 'summer_gold', 'summer_silver', 'summer_bronze',
                                  'summer_total']]

summer_middle_east.to_csv("data/summer_middle_east.csv", index=True)


summer_south_america = south_america[['countries', 'summer_participations', 'summer_gold', 'summer_silver',
                                      'summer_bronze', 'summer_total']]

summer_south_america.to_csv("data/summer_south_america.csv", index=True)


summer_north_america = north_america[['countries', 'summer_participations', 'summer_gold', 'summer_silver',
                                      'summer_bronze', 'summer_total']]

summer_north_america.to_csv("data/summer_north_america.csv", index=True)


summer_central_america = central_america[['countries', 'summer_participations', 'summer_gold', 'summer_silver',
                                          'summer_bronze', 'summer_total']]

summer_central_america.to_csv("data/summer_central_america.csv", index=True)


summer_europe = europe[['countries', 'summer_participations', 'summer_gold', 'summer_silver', 'summer_bronze',
                        'summer_total']]

summer_europe.to_csv("data/summer_europe.csv", index=True)


summer_oceania = oceania[['countries', 'summer_participations', 'summer_gold', 'summer_silver', 'summer_bronze',
                          'summer_total']]

summer_oceania.to_csv("data/summer_oceania.csv", index=True)


# subsetting for winter competitions only
winter_asia = asia[['countries', 'winter_participations', 'winter_gold', 'winter_silver', 'winter_bronze',
                    'winter_total']]

winter_asia.to_csv("data/winter_asia.csv", index=True)


winter_africa = africa[['countries', 'winter_participations', 'winter_gold', 'winter_silver', 'winter_bronze',
                        'winter_total']]

winter_africa.to_csv("data/winter_africa.csv", index=True)


winter_middle_east = middle_east[['countries', 'winter_participations', 'winter_gold', 'winter_silver', 'winter_bronze',
                                  'winter_total']]

winter_middle_east.to_csv("data/winter_middle_east.csv", index=True)


winter_south_america = south_america[['countries', 'winter_participations', 'winter_gold', 'winter_silver',
                                      'winter_bronze', 'winter_total']]

winter_south_america.to_csv("data/winter_south_america.csv", index=True)


winter_north_america = north_america[['countries', 'winter_participations', 'winter_gold', 'winter_silver',
                                      'winter_bronze', 'winter_total']]

winter_north_america.to_csv("data/winter_north_america.csv", index=True)


winter_central_america = central_america[['countries', 'winter_participations', 'winter_gold', 'winter_silver',
                                          'winter_bronze', 'winter_total']]

winter_central_america.to_csv("data/winter_central_america.csv", index=True)


winter_europe = europe[['countries', 'winter_participations', 'winter_gold', 'winter_silver', 'winter_bronze',
                        'winter_total']]

winter_europe.to_csv("data/winter_europe.csv", index=True)


winter_oceania = oceania[['countries', 'winter_participations', 'winter_gold', 'winter_silver', 'winter_bronze',
                          'winter_total']]

winter_oceania.to_csv("data/winter_oceania.csv", index=True)


# subsetting for total competitions
total_asia = asia[['countries', 'total_participation', 'total_gold', 'total_silver', 'total_bronze',
                   'total_total']]

total_asia.to_csv("data/total_asia.csv", index=True)


total_africa = africa[['countries', 'total_participation', 'total_gold', 'total_silver', 'total_bronze',
                       'total_total']]

total_africa.to_csv("data/total_africa.csv", index=True)


total_middle_east = middle_east[['countries', 'total_participation', 'total_gold', 'total_silver', 'total_bronze',
                                 'total_total']]

total_middle_east.to_csv("data/total_middle_east.csv", index=True)


total_south_america = south_america[['countries', 'total_participation', 'total_gold', 'total_silver', 'total_bronze',
                                     'total_total']]

total_south_america.to_csv("data/total_south_america.csv", index=True)


total_north_america = north_america[['countries', 'total_participation', 'total_gold', 'total_silver', 'total_bronze',
                                     'total_total']]

total_north_america.to_csv("data/total_north_america.csv", index=True)


total_central_america = central_america[['countries', 'total_participation', 'total_gold', 'total_silver',
                                         'total_bronze', 'total_total']]

total_central_america.to_csv("data/total_central_america.csv", index=True)


total_europe = europe[['countries', 'total_participation', 'total_gold', 'total_silver', 'total_bronze',
                       'total_total']]

total_europe.to_csv("data/total_europe.csv", index=True)


total_oceania = oceania[['countries', 'total_participation', 'total_gold', 'total_silver', 'total_bronze',
                         'total_total']]

total_oceania.to_csv("data/total_oceania.csv", index=True)
