import pandas as pd
import numpy as np
import os

folder_path = "C:/Users/Nasser/Desktop/AllaM"
quran_path="D:/projects/Quran-Grammar-Scraping/Quran_Grammar.csv"
paths=[]


for filename in os.listdir(folder_path):
    if "xlsx" in filename:
        file_path = os.path.join(folder_path, filename)
        paths.append(file_path)


def collect_data(files,all_data):
    for i in files:
        df=pd.read_excel(i)
        all_data = pd.concat([all_data,df ], ignore_index=True)
    return all_data



all_data=pd.DataFrame(columns=["verse","grammar","surah"])
all_data=collect_data(paths,all_data)


quran=pd.read_csv(quran_path,sep=';')

quran = pd.concat([quran,all_data ], ignore_index=True)
quran.to_csv('Quran.csv', index=False)