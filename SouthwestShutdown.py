# Ellie Shuo Jin
# PSY 394U
# 4.17.18
# Homework 4.2

# Import Libraries
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np

## 1. Constructing the airline network
# Loading Southwest Airline passenger data
routeData = pd.read_csv('Southwest_Mar2013.csv')

# Create a graph
G = nx.Graph()

# Loop over the routes
for iRoute in range(len(routeData)):
    # Add nodes
    origNode = routeData.loc[iRoute,'ORIGIN']
    destNode = routeData.loc[iRoute,'DEST']
    G.add_node(origNode)
    G.add_node(destNode)
    # Add edges
    if destNode not in G[origNode]:
        G.add_edge(origNode,destNode)

# Plot the network
plt.figure(figsize=[9,9])
pos = nx.kamada_kawai_layout(G, weight=None)
nx.draw_networkx_nodes(G, pos, node_color='lightblue')
nx.draw_networkx_edges(G, pos, edge_color='grey')
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')
plt.axis('off')
plt.title('Southwest Airlines Network')
plt.show()

## 2. Identifying 5 highest betweenness centrality nodes
# Betweenness centrality
C = nx.betweenness_centrality(G)

# Sort nodes by betweenness centrality
C_node = C.keys()
C_k = C.values()
sortedNodes = sorted(zip(C_node, C_k), key=lambda x: x[1], reverse=True)
sC_node, sC_k = zip(*sortedNodes)

# Top nodes and their betweenness centrality
print('Southwest Airlines -- Top degree centrality nodes')
print('Node             \tBetweenness centrality')
for iNode in range(5):
    print('%-16s\t' % str(sC_node[iNode]), end='')
    print('%6.4f' % sC_k[iNode])
print()

# Top betweenness centrality nodes:
# MCO 0.0968
# AUS 0.0743
# DEN 0.0563
# SLC 0.0323
# RDU 0.0246

## 3. Calculate relative giant component size and betweenness after virtual shutdown
# Remove the highest betweenness node from the network (i.e., MCO)
G_shutdown = G.copy()
G_shutdown.remove_node(sC_node[0])

# Calculate the relative giant component size of the resulting network after the deletion
GC_shutdown = len(sorted(nx.connected_components(G_shutdown), key = len, reverse=True)[0])
rGC_shutdown = GC_shutdown/len(G_shutdown.nodes())
print('Relative giant component size following MCO shutdown')
print('Southwest Airlines: %4.2f' % rGC_shutdown)
print()

# Relative giant component size following MCO shutdown
# Southwest Airlines: 0.96

# Re-calculate top 5 highest betweenness nodes and their centralities
# Re-calculate: Betweenness centrality
C_shutdown = nx.betweenness_centrality(G_shutdown)

# Re-calculate: Sort nodes by betweenness centrality
C_node2 = C_shutdown.keys()
C_k2 = C_shutdown.values()
sortedNodes2 = sorted(zip(C_node2, C_k2), key=lambda x: x[1], reverse=True)
sC_node2, sC_k2 = zip(*sortedNodes2)

# Re-calculate: Top nodes and their betweenness centrality
print('Southwest Airlines -- Top degree centrality nodes following MCO shutdown')
print('Node             \tBetweenness centrality')
for iNode in range(5):
    print('%-16s\t' % str(sC_node2[iNode]), end='')
    print('%6.4f' % sC_k2[iNode])

# Re-calculated top betweenness centrality nodes:
# AUS 0.0721
# DEN 0.0553
# SLC 0.0312
# EWR 0.0237
# RDU 0.0237
