import networkx as nx
import matplotlib.pyplot as plt
import itertools

# Generate a random graph of cities
num_cities = 5
graph = nx.complete_graph(num_cities)
for u, v in graph.edges():
    graph[u][v]['weight'] = round(100 * (1 + u + v), 2)

# Find the shortest route that visits all cities and returns to the starting city
shortest_route = None
shortest_length = float('inf')
for permutation in itertools.permutations(range(num_cities)):
    length = sum(graph[u][v]['weight'] for u, v in zip(permutation, permutation[1:] + permutation[:1]))
    if length < shortest_length:
        shortest_route = permutation
        shortest_length = length

# Print the shortest route and its length
print("Shortest route:", shortest_route)
print("Length:", shortest_length)

# Draw the graph with the shortest route highlighted
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True)
nx.draw_networkx_edges(graph, pos, edgelist=[(shortest_route[i], shortest_route[i+1]) for i in range(num_cities-1)] + [(shortest_route[-1], shortest_route[0])], edge_color='r', width=2)
plt.show()

