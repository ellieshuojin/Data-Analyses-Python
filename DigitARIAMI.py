import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score

# loading the digits data
digits = datasets.load_digits()
digitsX = digits.data    # the data, 1797 x 64 array
digitsImages = digits.images  # image data, 1797 x 8 x 8
digitsTargets = digits.target # target information
digitsFeatureNames = digits.target_names  # digits

# PCA with all possible components
digitsPCA = PCA(n_components=64)
digitsPCs = digitsPCA.fit_transform(digitsX)

# plotting the explained variance ratio (a.k.a., Scree plot)
plt.plot(np.arange(1,65),digitsPCA.explained_variance_ratio_)
plt.xlabel('Component number')
plt.ylabel('Proportion of explained variance')
plt.show()

# I conclude that 13 PCs are needed in the reduced data
PC = digitsPCs[:,:13]
# K-means clustering again
km = KMeans(n_clusters=10)  
km.fit(PC)  # fitting the principal components
y_cl = km.labels_   # clustering info resulting from K-means

y = digitsTargets
print('ARI=',adjusted_rand_score(y, y_cl),sep='')
print('AMI=',adjusted_mutual_info_score(y, y_cl),sep='')
