from collections import deque

# graph as adjacency lists (dictionary of lists)
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


print(graph)


# create queue
search_queue = deque()
search_queue += graph["you"]

while search_queue:

    person = search_queue.popleft()
    if p