### Step 1: Import Required Libraries
import datetime
from datetime import date, timedelta
import pandas as pd
import numpy as np
import yfinance as yf
import os
import shutil #deleting directories


### Step 2: Tickers and corresponding symbols
dict_symbols = {
    "ZN=F":["ZN","10-Year T-Note Futures"],
    "DX-Y.NYB":["DXY","US Dollar Index"],
    "CL=F":["CL","Crude Oil futures"],
    "GC=F":["GC","Gold futures"],
    "NQ=F":["NQ","Nasdaq 100 futures"],
    "^DJI":["DJI","Dow Jones Industrial Average"],
    "^GSPC":["GSPC","S&P 500"]}
    # "FGBL=F":["FGBL","German 10-Year Bund"]
    # "FOAT=F":["FOAT","French 10-year OAT"]
    # "G=F":["G", "UK 10-Year Gilt"]
print(dict_symbols)


### Step 3: Make Folders to Store Data
Intraday_data_files = "Intraday_data_files"
os.makedirs(Intraday_data_files, exist_ok=True)
Daily_backup_files="Daily_backup_files"
os.makedirs(Daily_backup_files, exist_ok=True)
os.makedirs('temp',exist_ok=True)#to create new files


### Step 4: Make Start-End Date Pairs
def make_start_end_pairs(days=29,steps=7):
    steps=-1*steps
    # Get today's date
    today = (datetime.datetime.now())
    end_intraday=(today-timedelta(days=1)).strftime("%Y-%m-%d")#doing this to get complete data of previous day
    start_intraday = (today - timedelta(days=days)).strftime("%Y-%m-%d")
    print(f'Fetching Intraday data (1m interval) from {start_intraday} to {end_intraday}')
    # Make List of all possible Start-End dates between today and today-30
    alldates=[]
    for i in range(days,0,steps):
        alldates.append((today-timedelta(days=i)).strftime("%Y-%m-%d"))
    grouped_start_last_dates=[[a,b] for a,b in zip(alldates,alldates[1:])]
    print('Date Intervals:',grouped_start_last_dates)
    return grouped_start_last_dates
grouped_start_last_dates=make_start_end_pairs(days=2,steps=1)


### Step5: Get data for all tickers for the given start-end date pairs
def combine_all_data(list_of_first_last,list_of_symbols): # Append the data for all the Start-End dates
    datalist=[]
    for data in list_of_first_last:
        start=data[0]
        end=data[1]
        interval='1m'
        data = yf.download(list_of_symbols, start=start, end=end, interval=interval) #Returns a dataframe
        datalist.append(data)
    return (pd.concat(datalist))


alltickers=list(dict_symbols.keys())
allsymbols=[i[0] for i in list(dict_symbols.values())]
print('Symbols',allsymbols)
print('Tickers',alltickers)
# Fetch Data
data = combine_all_data(grouped_start_last_dates,list_of_symbols=alltickers)
tickers_as_columns=data.stack(level=0,future_stack=False)
tickers_as_columns.index.names=['Datetime','Price']


### Step6: Store this data in Daily_backup_files folder
for col in tickers_as_columns.columns:
   
    col_data=tickers_as_columns[col].unstack()
    dict_symbols[col].append(col_data)
    start_date=grouped_start_last_dates[0][0]
    end_date=grouped_start_last_dates[-1][-1]
    start_end_date=f'Intraday_{dict_symbols[col][0]}_{start_date}_to_{end_date}.csv'
    col_data.to_csv(
        os.path.join(Daily_backup_files,start_end_date)
    )


names=[dict_symbols[key][0] for key in dict_symbols.keys()]
names


### Step7: Merge the newly created files with original files

for key in names:
    for entry in os.scandir(Daily_backup_files):
            if entry.is_file() and entry.name.endswith('.csv'):
                [_,ticker,newstart,_,newend]=(entry.name.replace('.csv',"")).split('_')
                if ticker==key and f'{newstart}_{newend}'==f'{grouped_start_last_dates[0][0]}_{grouped_start_last_dates[-1][-1]}':
                    newcsvpath=os.path.join(Daily_backup_files,entry.name)
                    newcsv=pd.read_csv(newcsvpath)
                    newcsv.reset_index(drop=True,inplace=True)

    for entry2 in os.scandir(Intraday_data_files):
            if entry2.is_file() and entry2.name.endswith('.csv'):
                oldcsvpath=os.path.join(Intraday_data_files,entry2.name)
                [_,_,ticker,oldstart,_,oldend]=(entry2.name.replace('.csv',"")).split('_')
                if ticker==key:
                    oldcsvpath=os.path.join(Intraday_data_files,entry2.name)
                    oldcsv=pd.read_csv(oldcsvpath)
                    oldcsv.reset_index(drop=True,inplace=True)
  
   
    finalcsv=pd.concat( (oldcsv,newcsv),axis=0)
    finalcsv.drop_duplicates(inplace=True)
    finalcsv.dropna(inplace=True)
    finalcsv.reset_index(drop=True,inplace=True)
    finalstart=str(finalcsv.iloc[0,0])[:10]
    finalend=str(finalcsv.iloc[(finalcsv.shape[0]-1),0])[:10]
    start_end=f'{finalstart}_to_{finalend}'
    finalpath=os.path.join('temp',f'Intraday_data_{key}_{start_end}.csv')
    finalcsv.to_csv(finalpath,index=False)

### Step8: Delete the Intraday_data_files directory and rename temp as that directory

#Delete
directory_path = Intraday_data_files
try:
    shutil.rmtree(directory_path)
    print(f"Directory {directory_path} and its contents deleted successfully.")
except FileNotFoundError:
    print("The directory does not exist.")
except PermissionError:
    print("You do not have the necessary permissions to delete this directory.")

#Rename
current_name = "temp"
new_name = "Intraday_data_files"

try:
    os.rename(current_name, new_name)
    print(f"Directory renamed from '{current_name}' to '{new_name}'")
except FileNotFoundError:
    print(f"Directory '{current_name}' not found!")
except PermissionError:
    print("You do not have permission to rename this directory.")
except Exception as e:
    print(f"An error occurred: {e}")