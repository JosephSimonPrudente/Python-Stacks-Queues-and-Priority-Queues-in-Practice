from graph import City, load_graph
import networkx as nx
print("_________________________________________________")
print(nx.nx_agraph.read_dot("roadmap.dot"))
print("_________________________________________________")
graph = nx.nx_agraph.read_dot("roadmap.dot")
print(graph.nodes["london"])

print("_________________________________________________")
nodes, graph = load_graph("roadmap.dot", City.from_dict)

print(nodes["london"])

print(graph)
print("_________________________________________________")
for neighbor in graph.neighbors(nodes["london"]):
    print(neighbor.name)
print("_________________________________________________")
for neighbor, weights in graph[nodes["london"]].items():
    print(weights["distance"], neighbor.name)
print("_________________________________________________")
def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(weights):
    return float(weights["distance"])

for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")
print("_________________________________________________")
