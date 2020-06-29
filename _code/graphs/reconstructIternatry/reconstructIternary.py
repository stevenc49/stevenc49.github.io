# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

def findTicketIndForStartCity(startCity):

    for ticketInd, cities in enumerate(tickets):
        if cities[0]==startCity:
            return ticketInd




tickets.sort(key=lambda x: x[1])


output = ['JFK']
for i in range(0, len(tickets)):

    currTicketIndex = findTicketIndForStartCity( output[-1] )
    nextCity = tickets[currTicketIndex][1]
    output.append(nextCity)

print(output)