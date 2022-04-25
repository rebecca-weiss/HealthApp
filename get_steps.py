import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
""" script to get steps data wanted from the all_records.csv file created in import_clean"""



all = pd.read_csv("apple_health_export/all_records.csv")

## get steps
steps_df = all[all['type'] == 'HKQuantityTypeIdentifierStepCount']


# convert dates to datetime
for date in ['creationDate', 'startDate', 'endDate']:
    steps_df[date] = pd.to_datetime(steps_df[date])


# make step counts numeric
steps_df.loc[:, 'value'] = pd.to_numeric(steps_df.loc[:, 'value'])

# only want apple watch data
steps_df = steps_df[steps_df['sourceName'] == 'Rebecca’s Apple\xa0Watch']

# drop unnecessary columns (all rows, columns 1-8)
steps_df = steps_df.iloc[:, 1:9]

# group steps by date
# steps_date = steps_df.groupby(['creationDate']).sum()

# change name to make simpler of type

# convert/string replace for easier naming
steps_df['type'] = steps_df['type'].str.replace('HKQuantityTypeIdentifier', '')

# write to csv
steps_df.to_csv("data/steps.csv", index=False)