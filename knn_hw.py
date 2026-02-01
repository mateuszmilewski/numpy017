import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X = np.array([
    [170, 65],
    [180, 80],
    [160, 50],
    [175, 70],
    [190, 95],
    [155, 48],
])
y = np.array([0, 1, 0, 0, 1, 0])  # class labels

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

new_people = np.array([[178, 72], [158, 52]])
print(knn.predict(new_people))
print(knn.predict_proba(new_people))  # probability per class
