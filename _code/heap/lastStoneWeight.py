import heapq

stones = [2,7,4,1,8,1]

def lastStoneWeight(stones):

    while len(stones)>=2:
    
        # negate values for max heap
        stones = list(map(lambda x: -x if x>0 else x, stones))
        # stones = [-x for x in stones if x>0 else x]
        print(stones)

        # get top 2 heaviest stones
        heapq.heapify(stones)
        print(stones)
        heavy1 = heapq.heappop(stones)
        heavy2 = heapq.heappop(stones)

        # smash the heaviest stones
        diff = abs(heavy1-heavy2)
        heapq.heappush(stones, diff)
        print(stones)

    print(stones)
    return stones[0]


print(lastStoneWeight(stones))