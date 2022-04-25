import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
from fxns import *
import datetime as dt


df = pd.read_csv("data/steps.csv", parse_dates=True)

# use function to convert dates to date values, get days/month/y
check_dates(df)

df['year'] = df['creationDate'].dt.year
df['month'] = df['creationDate'].dt.month
df['day_name'] = df['creationDate'].dt.day_name()
