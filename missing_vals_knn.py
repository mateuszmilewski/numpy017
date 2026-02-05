import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer

X = pd.DataFrame({
    "A": [1.0, 2.0, np.nan, 4.0, 5.0],
    "B": [np.nan, 20.0, 30.0, 40.0, 50.0],
    "C": [100.0, 200.0, 300.0, np.nan, 500.0],
})

imp = KNNImputer(n_neighbors=2, weights="distance")
X_filled = pd.DataFrame(imp.fit_transform(X), columns=X.columns)

print(X)
print(X_filled)
