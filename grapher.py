from typing import Dict, List
import networkx as nx


def removeNonKeyValues(data: Dict[str, List[str]]):
    keys = set(data.keys())
    for key, value in data.items():
        new_value = keys.intersection(value)
        data[key] = new_value
    return data


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

    data = removeNonKeyValues(data)

    graph = generateGraph(data)
    outputGraphImage(graph)
