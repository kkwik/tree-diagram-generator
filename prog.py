import networkx as nx
import matplotlib.pyplot as plt
import pydot

G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B','D')

PG = nx.nx_pydot.to_pydot(G)

PG.write_png('output.png')
