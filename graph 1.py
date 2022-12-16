from graph import City, load_graph
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