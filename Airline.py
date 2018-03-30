import networkx as nx
import pandas as pd

# loading the data
routeData = pd.read_csv('Southwest_Mar2013.csv')

# first, creating a graph
G=nx.Graph()

# loop over routes
for iRoute in range(len(routeData)):
    # adding nodes
    origNode = routeData.loc[iRoute,'ORIGIN']
    destNode = routeData.loc[iRoute,'DEST']
    wEdge = routeData.loc[iRoute,'PASSENGERS']
    G.add_node(origNode)
    G.add_node(destNode)
    # adding an edge if it does not alreay exist, with the weight
    if destNode not in G[origNode]:
        G.add_edge(origNode,destNode,weight=wEdge)
    else:
        G[origNode][destNode]['weight'] += wEdge


# just for fun, plotting the network
import matplotlib.pyplot as plt
import numpy as np

edgeweight = [ np.log10(d['weight']) for (u,v,d) in G.edges(data=True)]
plt.figure(figsize=[9,9])
pos = nx.kamada_kawai_layout(G, weight=None) # positions for all nodes
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, edge_color='lightblue', width=edgeweight)
nx.draw_networkx_labels(G, pos, font_size=10, font_color='DarkGreen')
plt.axis('off')
plt.title('Southwest Airlines network')
plt.show()
