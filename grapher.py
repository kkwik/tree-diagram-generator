from typing import Dict, List
import networkx as nx
import matplotlib.pyplot as plt
import pydot


def generateGraph(graphData: Dict[str, List[str]]):
    G = nx.Graph()

    for key in graphData:
        for value in graphData[key]:
            G.add_edge(key, value)

    return G


def outputGraphImage(graph: nx.Graph):
    PG = nx.nx_pydot.to_pydot(graph)

    PG.write_png('output.png')


if __name__ == '__main__':
    data = {'A': ['B', 'C'],
            'B': ['D']}

    graph = generateGraph(data)
    outputGraphImage(graph)