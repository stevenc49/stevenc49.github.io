costs = [
    [10,20],
    [30,200],
    [400,50],
    [30,20]
]

def minCosts(costs):

    n = len(costs)//2

    # calculate the difference between city A and city B for each person
    delta = [(a - b) for a, b in costs]
    print( "delta: ", delta )

    # get the ordered difference
    ordered_delta = sorted((value, i) for (i, value) in enumerate(delta))
    print( "ordered delta:", ordered_delta )
    
    minimum_cost = 0

    # for the n smallest cost_A - cost_B, it costs a lot to fly to B,
    # so we send them to city A
    print( "ordered_delta[:n] ", ordered_delta[:n] )
    for value, i in ordered_delta[:n]:
        minimum_cost += costs[i][0]

    # for the n greatest cost_A - cost_B, it costs a lot to fly to A,
    # so we send them to city B
    for value, i in ordered_delta[n:]:
        minimum_cost += costs[i][1]
    return minimum_cost

print( minCosts(costs) )