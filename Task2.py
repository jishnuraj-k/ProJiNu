## Downsampling
import pandas as pd
#detail
def detailDownsampled():
    data=pd.read_csv("detail.csv",parse_dates =['Absolute Time'], index_col ='Absolute Time') #reading the csv file that was saved in task 1 and setting Absolute time as index column 
    data.drop(['Record Index'], axis='columns', inplace=True) # Droping Record index column as its not neccessary
    detail_resampled = data.resample('1 min').mean() #sampling the dataset (Taking subsets (means)) at 1 sample/minute
    detail_resampled.to_csv('detailDownsampled.csv') #saving the dataframe as csv file

#detailTemp
def detailTempDownsampled():
    data=pd.read_csv("detailTemp.csv",parse_dates =['Realtime'], index_col ='Realtime') #reading the csv file that was saved in task 1 and setting Absolute time as index column 
    data.drop(['Record ID'], axis='columns', inplace=True) # Droping Record id column as its not neccessary
    detailTemp_resampled = data.resample('1 min').mean() #sampling the dataset (Taking subsets (means)) at 1 sample/minute
    detailTemp_resampled.to_csv('detailTempDownsampled.csv') #saving the dataframe as csv file

#detailVol
def detailVol_resample():
    data=pd.read_csv("detailVol.csv",parse_dates =['Realtime'], index_col ='Realtime') #reading the csv file that was saved in task 1 and setting Absolute time as index column 
    data.drop(['Record ID'], axis='columns', inplace=True) # Droping Record id column as its not neccessary
    detailVol_resampled = data.resample('1 min').mean() #sampling the dataset (Taking subsets (means)) at 1 sample/minute
    detailVol_resampled.to_csv('detailVolDownsampled.csv') #saving the dataframe as csv file

detailDownsampled()
detailVol_resample()  
detailTempDownsampled()
