import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn import datasets

# loading the iris data
iris = datasets.load_iris()
X = iris.data    # Data
y = iris.target  # Target i.e., true clusters
numClus = 3  # number of clusters

# hierarchical clustering, unlike k-means clustering which yields clusters of similar sizes, hierarchical clustering may produce clusters of heterogeneous sizes
hc = AgglomerativeClustering(n_clusters=3)  # defining the clustering object
hc.fit(X)  # actually fitting the data
y_clus = hc.labels_   # clustering info resulting from hieararchical

### plotting the clusters
plt.figure(figsize=[8,4])

# first, results from hierarchical
plt.subplot(121)
plt.scatter(X[:,3],X[:,0],c=y_clus,marker='+')
plt.xlabel('Petal width')
plt.ylabel('Sepal length')
plt.title('Clusters from hierarchical')

# as a comparison, the true clusters
plt.subplot(122)
plt.scatter(X[:,3],X[:,0],c=y,marker='+')
plt.xlabel('Petal width')
plt.ylabel('Sepal length')
plt.title('True clusters')

plt.show()

# cluster sizes
# from hierarchical
cs_hc = [len(y_clus[y_clus==i]) for i in range(3)]
print(cs_hc)
# true target
cs_target = [len(y[y==i]) for i in range(3)]
print(cs_target)
