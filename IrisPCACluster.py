import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn import datasets


# Loading the iris data
iris = datasets.load_iris()
X = iris.data    # Data
y = iris.target  # Target i.e., true clusters
numClus = 3  # number of clusters

# Applying PCA first
pca = PCA(n_components=2)
X_r = pca.fit_transform(X)  # Principal components

# K-means clustering
km = KMeans(n_clusters=3)  # defining the clustering object
km.fit(X_r)  # fitting the principal components
y_clus = km.labels_   # clustering info resulting from K-means


### plotting the clusters
plt.figure(figsize=[8,4])
# First, results from K-means
plt.subplot(121)
plt.scatter(X_r[:,0],X_r[:,1],c=y_clus)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('Clusters from K-means')

# As a comparison, the true clusters
plt.subplot(122)
plt.scatter(X_r[:,0],X_r[:,1],c=y)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('True clusters')

plt.show()

