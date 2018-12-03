import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

k_value = []
SSE = []

sc = MinMaxScaler(feature_range=(0,1))

dataset = pd.read_csv("Churn-Modelling.csv")
dataset = dataset.iloc[:,[8,12]]

X = np.array(dataset)
X = sc.fit_transform(X)

for i in range(1, 15):
    k_means = KMeans(n_clusters = i)
    k_means = k_means.fit(X)
    
    SSE.append(np.float64(k_means.inertia_))
    k_value.append(i)

plt.plot(k_value, SSE)
plt.xlabel("K Values")
plt.ylabel("Sum of square distances")
plt.show()




