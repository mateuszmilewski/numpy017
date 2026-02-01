import numpy as np
from sklearn.impute import KNNImputer

X = np.array([
    [1, 10, 100],
    [2, 11, np.nan],
    [1, 9, 95],
    [10, 50, 500]
])

imputer = KNNImputer(n_neighbors=2)
X_imputed = imputer.fit_transform(X)

print(X_imputed)
