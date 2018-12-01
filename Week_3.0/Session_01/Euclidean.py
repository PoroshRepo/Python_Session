import numpy as np
import pandas as pd
from scipy.spatial import distance


train = pd.read_csv("dataset/ECG200_TRAIN.csv", header = None)
test = pd.read_csv("dataset/ECG200_TEST.csv", header = None)

train = train.iloc[:, 1:]
test = test.iloc[:, 1:]

train = np.array(train)
test = np.array(test)

distances = []

#With for loop
for a,b in zip(train, test):
    distances.append(np.linalg.norm(a-b))
    
avg_dist = np.mean(distances) 





