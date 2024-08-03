from sklearn.decomposition import PCA
import numpy as np

# Example data
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

# Model
pca = PCA(n_components=1)
X_reduced = pca.fit_transform(X)

print("Reduced Data:", X_reduced)
