# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:49:46 2022

@author: Dolagy Baky
"""




import random

import matplotlib.pyplot as plt
import networkx as nx
    
import matplotlib.pyplot as plt
    
G = nx.Graph()
nx.add_cycle(G,[0, 1, 2, 3])
nx.add_cycle(G,[4, 5, 6, 7])
G.add_edge(0, 7)
nx.draw(G, with_labels=True)  


partition = [
    {1, 2, 3},
    {4, 5, 6},
    {0, 7},
]



nx.community.is_partition(G, partition)
partition_map = {}
for idx, cluster_nodes in enumerate(partition):
    for node in cluster_nodes:
        partition_map[node] = idx

partition_map
print(partition_map)

print(partition_map[0] == partition_map[7])


node_colors = [partition_map[n] for n in G.nodes]
        
nx.draw(G, node_color=node_colors, with_labels=True)



def modularity(G, partition):
    W = sum(G.edges[v, w].get('weight', 1) for v, w in G.edges)
    summation = 0
    for cluster_nodes in partition:
        s_c = sum(G.degree(n, weight='weight') for n in cluster_nodes)
        # Use subgraph to count only internal links
        C = G.subgraph(cluster_nodes)
        W_c = sum(C.edges[v, w].get('weight', 1) for v, w in C.edges)
        summation += W_c - s_c ** 2 / (4 * W)
    
    return summation / W


modularity(G, partition)



partition_2 = [
    {0, 1, 2, 3},
    {4, 5, 6, 7},
]
print(modularity(G, partition_2))

print(nx.community.quality.modularity(G, partition_2))



K = nx.karate_club_graph()
nx.draw(K, with_labels=True)

K.nodes[0]


K.nodes[9]


K = nx.karate_club_graph()
club_color = {
    'Mr. Hi': 'orange',
    'Officer': 'lightblue',
}
node_colors = [club_color[K.nodes[n]['club']] for n in K.nodes]
nx.draw(K, node_color=node_colors, with_labels=True)



groups = {
    'Mr. Hi': set(),
    'Officer': set(),
}

for n in K.nodes:
    club = K.nodes[n]['club']
    groups[club].add(n)
    
print(groups)


empirical_partition = list(groups.values())
print(empirical_partition)


print(nx.community.is_partition(K, empirical_partition))

print(nx.community.quality.modularity(K, empirical_partition))


G = nx.karate_club_graph()
nx.draw(G)

print(nx.edge_betweenness_centrality(G))

my_edge_betweenness = nx.edge_betweenness_centrality(G)
my_edge_betweenness[0, 1]


my_edge_betweenness.get((0, 1))

print(max(my_edge_betweenness, key=my_edge_betweenness.get))
print(max(G.edges(), key=my_edge_betweenness.get))


my_edge_betweenness = nx.edge_betweenness_centrality(G)
most_valuable_edge = max(G.edges(), key=my_edge_betweenness.get)
G.remove_edge(*most_valuable_edge)

nx.connected_components(G)
print(list(nx.connected_components(G)))



G = nx.karate_club_graph()
partition_sequence = []
for _ in range(G.number_of_edges()):
    my_edge_betweenness = nx.edge_betweenness_centrality(G)
    most_valuable_edge = max(G.edges(), key=my_edge_betweenness.get)
    G.remove_edge(*most_valuable_edge)
    my_partition = list(nx.connected_components(G))
    partition_sequence.append(my_partition)



len(partition_sequence), nx.karate_club_graph().number_of_edges()
len(partition_sequence[0])

len(partition_sequence[-1]), nx.karate_club_graph().number_of_nodes

G = nx.karate_club_graph()
modularity_sequence = [modularity(G, p) for p in partition_sequence]
modularity_sequence



plt.plot(modularity_sequence)
plt.ylabel('Modularity')
plt.xlabel('Algorithm step')


def my_modularity(partition):
    return nx.community.quality.modularity(G, partition)
best_partition = max(partition_sequence, key=my_modularity)

best_partition

def create_partition_map(partition):
    partition_map = {}
    for idx, cluster_nodes in enumerate(partition):
        for node in cluster_nodes:
            partition_map[node] = idx
    return partition_map


best_partition_map = create_partition_map(best_partition)

node_colors = [best_partition_map[n] for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors)


nx.community.quality.modularity(G, best_partition)



for partition in partition_sequence:
    if len(partition) == 2:
        two_cluster_partition = partition
        break

two_cluster_partition

two_cluster_partition_map = create_partition_map(two_cluster_partition)

node_colors = [two_cluster_partition_map[n] for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors)

nx.community.quality.modularity(G, two_cluster_partition)




pos = nx.layout.spring_layout(G)
fig = plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
two_cluster_partition_map = create_partition_map(two_cluster_partition)
node_colors = [two_cluster_partition_map[n] for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors, pos=pos)
plt.title('Predicted communities')

plt.subplot(1, 2, 2)
node_colors = [G.nodes[n]['club'] == 'Officer' for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors, pos=pos)
plt.title('Actual communities')

G.nodes[8]
print(list(nx.community.girvan_newman(G))[:5])











































































































































