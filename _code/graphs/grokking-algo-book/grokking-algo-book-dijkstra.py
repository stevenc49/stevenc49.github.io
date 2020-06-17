


# dijkstra needs 3 hashtables and a list to keep track of processed nodes
graph = {}
costs = {}
parents = {}

processed = []

# graph: a hashtable of more hash tables to store edges and weights
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}



# costs: a hashtable to store costs of each node
infinity = float("inf")
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity


# parents hashtable
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None




print( graph )
print( costs )
print( parents )
