import matplotlib.pyplot as plt  
import numpy as np  
from sklearn.cluster import KMeans 
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

k_value = []
SSE = []

sc = MinMaxScaler(feature_range=(0,1))

dataset = pd.read_csv("Churn-Modelling.csv")
dataset = dataset.iloc[:,[8,12]]
X = np.array(dataset)
X = sc.fit_transform(X)
###################################################

k_means = KMeans(n_clusters = 4)
k_means = k_means.fit(X)

labels = k_means.labels_
centers = k_means.cluster_centers_

plt.scatter(X[:,0], X[:,1], c = k_means.labels_, cmap='rainbow')  
plt.scatter(k_means.cluster_centers_[:,0] ,k_means.cluster_centers_[:,1], color='black')