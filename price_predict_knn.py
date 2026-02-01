import numpy as np
from sklearn.neighbors import KNeighborsRegressor

X = np.array([
    [1.2, 10],
    [1.6, 7],
    [2.0, 4],
    [1.4, 12],
    [2.5, 2],
    [1.8, 6],
])
y = np.array([9000, 12000, 18000, 8000, 26000, 15000])

knn = KNeighborsRegressor(n_neighbors=2, weights="distance")
knn.fit(X, y)

print("price prediction: ", knn.predict(np.array([[1.7, 5], [2.3, 3]])))