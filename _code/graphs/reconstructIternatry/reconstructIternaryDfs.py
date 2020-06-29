tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

def findTicketIndForStartCity(startCity):

    graph = {}
    
    tickets.sort(key=lambda x: x[1])

    # add all to graph hashmap
    for u, v in tickets:
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
    
    # put jfk on stack
    itinerary, stack = [], [("JFK")]
    
    while stack:
        curr = stack[-1]
        
        if curr in graph and len(graph[curr]) > 0:
            stack.append(graph[curr].pop(0))
        else:
            itinerary.append(stack.pop())
    return itinerary[::-1]


print( findTicketIndForStartCity(tickets) )