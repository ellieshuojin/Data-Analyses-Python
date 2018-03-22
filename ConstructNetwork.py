import networkx as nx
import matplotlib.pyplot as plt

# a list of emplyees on the same shift
listWorkers = [['Manager1', 1, 3, 4, 5],
               ['Manager1', 1, 2, 3],
               ['Manager1', 3, 5, 6, 7],
               ['Manager1', 1, 7, 8],
               ['Manager1', 2, 4, 6, 7],
               ['Manager2', 4, 8, 9, 10, 11],
               ['Manager2', 8, 10, 11, 12]]

# this dataset shows which employees work together this particular week.
# there is a for loop over different days of the week, and within that for loop is another for loop for employees working on that day.
# employees are added to the network as a node, if they are not already in the network (i.e., iNode not in G).
# when the for loop for employees are done, then edges are added with nested for loops.
# if two employees are not connected (i.e. jNode not in G[iNode]), then an edge is added between them.
# if they are connected, then the edge weight is increased by 1.

# first, creating a graph
G=nx.Graph()

# loop over days
for iDay in range(len(listWorkers)):
    # adding nodes. Check if node exists first before adding
    for iNode in listWorkers[iDay]:
        if iNode not in G:
            G.add_node(iNode)
    # adding edges. Check if edge exists before adding
    for i,iNode in enumerate(listWorkers[iDay]):
        for j,jNode in enumerate(listWorkers[iDay],i+1):
            # if iNode and jNode are not connected
            if (iNode!=jNode) and (jNode not in G[iNode]):  
                G.add_edge(iNode,jNode,weight=1.0)
            # if iNode and jNode are connected            
            elif iNode!=jNode:  
                G[iNode][jNode]['weight'] += 1.0

# drawing the graph  --- Kamada-Kawai layout
pos = nx.kamada_kawai_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos)

# edges
edgeweight = [ d['weight'] for (u,v,d) in G.edges(data=True)]
nx.draw_networkx_edges(G, pos, width=edgeweight)

# labels
nx.draw_networkx_labels(G, pos)

plt.axis('off')
plt.show()

# Saving the graph in different formats
# adjacency list
nx.write_adjlist(G,'CoWorking.adjllist')

# edge list
nx.write_edgelist(G,'CoWorking.edgelist')

# GML
nx.write_gml(G,'CoWorking.gml')


# loading the graph
Gadj = nx.read_adjlist('CoWorking.adjllist')

Gedge = nx.read_edgelist('CoWorking.edgelist')

Ggml = nx.read_gml('CoWorking.gml')
