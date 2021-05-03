import os
import pandas as pd

#Subtask 1

path = r'C:\Users\Jishnuraj k\Desktop\CSVFILES' #Path to the csv files that are obtained from the xlxs sheets using visual basics

def detail():
    files = os.listdir(path)
    files_xls = [f for f in files if f[:10] == 'Detail_67_'] #Accessing DetailTVol_67_ csv files and storing its name to a list
    df = pd.DataFrame()  
    #Accessing each csv files one by one and appending to  a dataframe by their name
    for f in files_xls:
        data = pd.read_excel(path+"/"+f)
        df = df.append(data)
    df.sort_values(by='Record Index') # For avoiding parity problem sorrting the dataframe with respect to record index
    df.to_csv('detail.csv',index=False) #saving the dataframe as csv

#Subtask 2
def detailVol():
    files = os.listdir(path)
    files_xls = [f for f in files if f[:9] == 'DetailVol'] #Accessing DetailTVol_67_ csv files and storing its name to a list
    df = pd.DataFrame()
    #Accessing each csv files one by one and appending to  a dataframe by their name
    for f in files_xls:
        data = pd.read_excel(path+"/"+f)
        df = df.append(data)
    df.sort_values(by='Record ID') # For avoiding parity problem sorrting the dataframe with respect to record id
    df.to_csv('detailVol.csv',index=False) #saving the dataframe as csv

#Subtask 3
def detailTemp():
    files = os.listdir(path)
    files_xls = [f for f in files if f[:10] == 'DetailTemp'] #Accessing DetailTemp_67_ xlxs files and storing its name to a list
    df = pd.DataFrame()
    #Accessing each csv files one by one and appending to  a dataframe by their name
    for f in files_xls: 
        data = pd.read_excel(path+"/"+f)
        df = df.append(data)
    df.sort_values(by='Record ID') # For avoiding parity problem sorrting the dataframe with respect to record id
    df.to_csv('detailTemp.csv',index=False) #saving the dataframe as csv
#Calling each function
detail()
detailVol()
detailTemp()