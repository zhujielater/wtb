import pandas as pd
from datetime import datetime

#------------------------------
#-- Read in Asset_Daily_View --
#------------------------------
df = pd.read_csv('BTC.csv')

#--------------------
#-- Apply strategy --
#--------------------
# need to convert text to date
# ref code: raw_data['Mycol'] = pd.to_datetime(raw_data['Mycol'], format='%d%b%Y:%H:%M:%S.%f')

df['Date'] = pd.to_datetime(df['Date'], format='%b %d, %Y')
df = df.set_index('Date') # need to have df = in the front... do I have to sort it?
df.sort_index(inplace=True)

# (use mod to implement fixed investment strategy)
# ref code: df['returns'] = np.log(df['closeAsk'] / df['closeAsk'].shift(1))  # 12

df['cons_date'] = pd.to_datetime("1900-01-01") # create a constant datetime series in pandas
df['date_diff'] = df['cons_date'] - df.index.to_series() # make it timedeltas

# if it is the 30th day, add position by 1 unit
# mod date_diff by 30
df['pos_chg'] = (df['date_diff'].dt.days%30 == 0)*1 # to improve code, and better document
df.info()

#-----------------------------
#--- CumSum then Final Plot --
#-----------------------------
# pct_return = market_value / cost - 1
# market_value = 
# ref code: 
#   df[strats].dropna().cumsum().apply(np.exp).plot()  # 24

# Write csv
