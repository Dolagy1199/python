# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:51:35 2022

@author: Dolagy Baky
"""

#The import statement
import networkx as nx



nx.__version__


#Creating and drawing undirected graphs

G = nx.Graph()
G.add_node('a')
nodes_to_add = ['b', 'c', 'd']
G.add_nodes_from(nodes_to_add)
G.add_edge('a', 'b')
edges_to_add = [('a', 'c'), ('b', 'c'), ('c', 'd')]
G.add_edges_from(edges_to_add)

nx.draw(G, with_labels=True)
nx.draw(G,
        with_labels=True,
        node_color='blue',
        node_size=1600,
        font_color='white',
        font_size=16,
        )

#Graph methods


G.nodes()

G.edges()

for node in G.nodes:
    print(node)


for edge in G.edges:
    print(edge)

G.number_of_nodes()

G.number_of_edges()

G.neighbors('b')

for neighbor in G.neighbors('b'):
    print(neighbor)

list(G.neighbors('b'))


#NetworkX functions vs. Graph methods

nx.is_tree(G)
nx.is_connected(G)

#Node and edge existence

G.has_node('a')

G.has_node('x')

'd' in G.nodes
G.has_edge('a', 'b')

G.has_edge('a', 'd')

('c', 'd') in G.edges

#Node degree


len(list(G.neighbors('a')))

G.degree('a')



#EXERCISE 1




def get_leaves(G):
   listWithOneDegree=[]
   for node in G.nodes:
       if(G.degree(node) == 1):
           listWithOneDegree.append(node)
   return listWithOneDegree

G = nx.Graph()
G.add_edges_from([
        ('a', 'b'),
        ('a', 'd'),
        ('c', 'd'),
    ])
assert set(get_leaves(G)) == {'c', 'b'}

items = ['spider', 'y', 'banana']
[item.upper() for item in items]


print(G.nodes())
print([G.degree(n) for n in G.nodes()])
g = (len(item) for item in items)
list(g)
max(len(item) for item in items)
sorted(item.upper() for item in items)


#Node names




G = nx.Graph()

G.add_nodes_from(['cat','dog','virus',13])

G.add_edge('cat','dog')

nx.draw(G, with_labels=True, font_color='white', node_size=1000)



print(open('./friends.adjlist').read())



SG = nx.read_adjlist('./friends.adjlist')


nx.draw(SG, node_size=2000, node_color='lightblue', with_labels=True)


SG.degree('Alice')



#EXERCISE 2

def max_degree(G):
    friendName = ""
    maxDegree = -1
    for node in G.nodes:
        if(G.degree(node) >= maxDegree):
            maxDegree = G.degree(node)
            friendName = node
    return (friendName,maxDegree)
SG = nx.read_adjlist('./friends.adjlist')
assert max_degree(SG) == ('Claire', 4)


#EXERCISE 3

def mutual_friends(G, node_1, node_2):
    friendNode1 = list(G.neighbors(node_1))
    friendNode2 = list(G.neighbors(node_2))
    listCommonFriend=[]
    for friend1 in friendNode1:
        for friend2 in friendNode2:
            if(friend1 == friend2):
                listCommonFriend.append(friend1)
                break
    return listCommonFriend
SG = nx.read_adjlist('./friends.adjlist')
assert mutual_friends(SG, 'Alice', 'Claire') == ['Frank']
assert mutual_friends(SG, 'George', 'Bob') == []
assert sorted(mutual_friends(SG, 'Claire', 'George')) == ['Dennis', 'Frank']




#Directed graphs
D = nx.DiGraph()

D.add_edges_from([(1,2),(2,3),(3,2),(3,4),(3,5),(4,5),(4,6),(5,6),(6,4),(4,2)])

nx.draw(D, with_labels=True)




D.has_edge(1,2)

D.has_edge(2,1)

print('Successors of 2:', list(D.successors(2)))

print('Predecessors of 2:', list(D.predecessors(2)))































































































