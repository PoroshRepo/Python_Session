import pandas as pd

#Reading the csv file
dataframe = pd.read_csv("dataset/ECG200_TRAIN.csv", header = None)

#Select a subset of the overall dataframe

range_chunked_dataframe = dataframe.iloc[0:10 , 1:]


index = [23,56,21,98,56]
specific_chunked_dataframe = dataframe.iloc[index ,1:]

print("Shape of the dataframe is row: "+str(dataframe.shape[0])+" column: "+str(dataframe.shape[1]))

