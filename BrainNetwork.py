# Ellie Shuo Jin
# PSY 394U
# 4.17.18
# Homework 4.1

# Import Libraries
from networkx.algorithms.community import label_propagation_communities
from networkx.algorithms.community import modularity
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Parameters
threshR = 0.5 # Threshold for the correlation matrix

# Loading the brain fMRI data
infile = np.load('CorrMat_Brain.npz')
R = infile['R']
nodeName = infile['nodeName']

# Getting the row and column indices for correlation exceeding 
# The predefined threshold threshR
rowInd, colInd = (R>0.5).nonzero()

## 1. Constructing the brain fMRI network based on the data
# Create a graph
G = nx.Graph()

# Add nodes
for iNode in range(len(nodeName)):
    G.add_node(iNode)
    
# Add edges
for i in range(len(rowInd)):
    G.add_edge(rowInd[i],colInd[i])

# Add labels
labels = {}
for i in range(90):
    labels[i] = nodeName[i]

# Plotting the figure
plt.figure(figsize=[11,11])
pos = nx.kamada_kawai_layout(G, weight=None)
nx.draw_networkx_nodes(G, pos, node_color='lightblue')
nx.draw_networkx_edges(G, pos, edge_color='grey')
nx.draw_networkx_labels(G, pos, labels, font_size=10, font_color='black')
plt.axis('off')
plt.title('Brain fMRI Network (original)')
plt.show()

## 2. Identifying communities in the network
# Community detection with the label propagation algorithm
commIndSet_G = label_propagation_communities(G)
commInd_lp = [list(x) for x in iter(commIndSet_G)]

# Plotting resulting communities in different colors
plt.figure(figsize=[11,11])
for iComm in range(len(commInd_lp)):
    nx.draw_networkx_nodes(G, pos, nodelist=commInd_lp[iComm],
                           cmap=plt.cm.rainbow,
                           vmin=0, vmax=len(commInd_lp)-1,
                           node_color = [iComm]*len(commInd_lp[iComm]),
                           node_size=300)
nx.draw_networkx_edges(G, pos, edge_color='grey')
nx.draw_networkx_labels(G, pos, labels, font_size=10, font_color='black')
plt.title('Brain fMRI Network (label propagation)')
plt.axis('off')
plt.show()

# Modularity calculation
mod_lp = modularity(G, commInd_lp)
print('Modularity of Brain fMRI Network (lable propagation): %6.4f' % mod_lp)
print()

## 3. Identifying the default mode network
roi = list(labels.keys())[list(labels.values()).index('Cingulum_Post_L')] # Identify the associated node number for region of interest (roi): posterior cingulate gyrus
community = ((np.array([(i, colour.index(roi)) for i,
                  colour in enumerate(commInd_lp)
                  if roi in colour]))[0])[0] # Identify the index of module containing the other nodes in the DMN
dmn = np.array(commInd_lp[community]) # Identify node numbers of all the nodes in the DMN
print('Default mode network (DMN) nodes:') # Print list of nodes in the DMN
for i in dmn:
    print(labels[i])
