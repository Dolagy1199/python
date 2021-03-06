# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:33:17 2022

@author: Dolagy Baky
"""

import random
import matplotlib.pyplot as plt
from collections import Counter
import statistics
import networkx as nx


G = nx.read_edgelist('.\datasets\ia-enron-only\ia-enron-only.edges', nodetype=int)
print(nx.info(G))
nx.draw(G)




max([1,2,3,4,5])
print(max(['apple', 'grape', 'carrot']))
print(max(['apple', 'grape', 'carrot'], key=len))






highest_degree_node = max(G.nodes, key=G.degree)
print(highest_degree_node)

G.degree(highest_degree_node)


betweenness = nx.centrality.betweenness_centrality(G)
highest_betweenness_node = max(G.nodes, key=betweenness.get)
print(highest_betweenness_node)

print(betweenness[highest_betweenness_node])



degree_sequence = [G.degree(n) for n in G.nodes]




print('Mean degree:', statistics.mean(degree_sequence))
print('Median degree:', statistics.median(degree_sequence))


betweenness = nx.centrality.betweenness_centrality(G)
betweenness_sequence = list(betweenness.values())

print('Mean betweenness:', statistics.mean(betweenness_sequence))
print('Median betweenness:', statistics.median(betweenness_sequence))



degree_counts = Counter(degree_sequence)
degree_counts



min_degree, max_degree = min(degree_counts.keys()), max(degree_counts.keys())

plot_x = list(range(min_degree, max_degree + 1))

plot_y = [degree_counts.get(x, 0) for x in plot_x]


plt.bar(plot_x, plot_y)


counts, bins, patches = plt.hist(betweenness_sequence, bins=10)

print(bins)
print(counts)


nx.connected_components(G)

core = next(nx.connected_components(G))
core

print(core)

print(len(core))

components = list(nx.connected_components(G))

print(len(components))



C = G.copy()

nodes_to_remove = random.sample(list(C.nodes), 2)
C.remove_nodes_from(nodes_to_remove)
print(C.remove_nodes_from(nodes_to_remove))



number_of_steps = 25
M = G.number_of_nodes() // number_of_steps
print(M)


num_nodes_removed = range(0, G.number_of_nodes(), M)



N = G.number_of_nodes()
C = G.copy()
random_attack_core_proportions = []
for nodes_removed in num_nodes_removed:
    # Measure the relative size of the network core
    core = next(nx.connected_components(C))
    core_proportion = len(core) / N
    random_attack_core_proportions.append(core_proportion)
    
    # If there are more than M nodes, select M nodes at random and remove them
    if C.number_of_nodes() > M:
        nodes_to_remove = random.sample(list(C.nodes), M)
        C.remove_nodes_from(nodes_to_remove)
        
      
plt.title('Random failure')
plt.xlabel('Number of nodes removed')
plt.ylabel('Proportion of nodes in core')
plt.plot(num_nodes_removed, random_attack_core_proportions, marker='o')
        
        
        
nodes_sorted_by_degree = sorted(G.nodes, key=G.degree, reverse=True)
top_degree_nodes = nodes_sorted_by_degree[:M]
print(top_degree_nodes)
        
N = G.number_of_nodes()
number_of_steps = 25
M = N // number_of_steps

num_nodes_removed = range(0, N, M)
C = G.copy()
targeted_attack_core_proportions = []
for nodes_removed in num_nodes_removed:
    # Measure the relative size of the network core
    core = next(nx.connected_components(C))
    core_proportion = len(core) / N
    targeted_attack_core_proportions.append(core_proportion)
    
    # If there are more than M nodes, select top M nodes and remove them
    if C.number_of_nodes() > M:
        nodes_sorted_by_degree = sorted(C.nodes, key=C.degree, reverse=True)
        nodes_to_remove = nodes_sorted_by_degree[:M]
        C.remove_nodes_from(nodes_to_remove)
        
        
plt.title('Targeted attack')
plt.xlabel('Number of nodes removed')
plt.ylabel('Proportion of nodes in core')
plt.plot(num_nodes_removed, targeted_attack_core_proportions, marker='o') 
        




plt.title('Random failure vs. targeted attack')
plt.xlabel('Number of nodes removed')
plt.ylabel('Proportion of nodes in core')
plt.plot(num_nodes_removed, random_attack_core_proportions, marker='o', label='Failures')
plt.plot(num_nodes_removed, targeted_attack_core_proportions, marker='^', label='Attacks')
plt.legend()




        
        
        










































