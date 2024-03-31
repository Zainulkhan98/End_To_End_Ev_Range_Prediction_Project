
# specifying columns for imputation
impute_col_most_freq = ['County','City','Postal Code','Vehicle Location','Electric Utility','2020 Census Tract']
impute_col_median = ['Legislative District']#try removing legislative district(so many null values, very skewed)

# specifying columns for one hot encoding
categorical_col_encoding = ['County','City','State','Postal Code','Make','Model','Electric Vehicle Type','Clean Alternative Fuel Vehicle (CAFV) Eligibility','Vehicle Location','Electric Utility','2020 Census Tract']# try ,'Model Year' later

['Electric Range','Base MSRP','DOL Vehicle ID','Legislative District']