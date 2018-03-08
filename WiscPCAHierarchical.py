import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering

# loadin the data
wiscData = pd.read_csv('wiscsem.txt', sep='\t')
wiscFeatures = np.array(wiscData.iloc[:,2:13])
featureNames = np.array(wiscData.columns[2:13])

# applying PCA
pca = PCA()  # creating a PCA transformation object
wiscPCs = pca.fit_transform(wiscFeatures) # fit the data

# Squared error plot
plt.plot(np.arange(1,len(featureNames)+1), pca.explained_variance_ratio_)
plt.xlabel('Component number')
plt.ylabel('Explained variance')
plt.show()

## We will use first two components
PC = wiscPCs[:,:2]


# determinging the number of clusters (up to 20 clusters)
SSE = []
for iClus in range(1,21):  
    # K-means clustering
    km = KMeans(n_clusters=iClus)  # K-means with a given number of clusters
    km.fit(PC)  # fitting the principal components
    SSE.append(km.inertia_) # recording the sum of square distances

# plotting the sum of square distance
plt.plot(np.arange(1,21),SSE,marker = "o")
plt.xlabel('Number of clusters')
plt.ylabel('Sum of sq distances')
plt.show()


## We will go with 3 clusters
# hierarchical clustering
hc = AgglomerativeClustering(n_clusters=3)  
hc.fit(PC)  # fitting the principal components
y_clus = hc.labels_   # clustering info resulting from hierarchical

# as a comparison, K-means clustering again
km = KMeans(n_clusters=3)  
km.fit(PC)  # fitting the principal components
y_clus_km = km.labels_   # clustering info resulting from K-means


### plotting the clusters
plt.figure(figsize=[8,4])
# First, hiearchical clustering
plt.subplot(121)
plt.scatter(PC[:,0],PC[:,1],c=y_clus,marker='+')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('Clusters from hierarchical (PC)')

# as a comparison, K-means clustering
plt.subplot(122)
plt.scatter(PC[:,0],PC[:,1],c=y_clus_km,marker='+')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('Clusters from K-means (PC)')

plt.show()


# Cluster sizes
# From hierarchical
cs_hc = [len(y_clus[y_clus==i]) for i in range(3)]
print(cs_hc)

# From K-means
cs_km = [len(y_clus_km[y_clus_km==i]) for i in range(3)]
print(cs_km)

