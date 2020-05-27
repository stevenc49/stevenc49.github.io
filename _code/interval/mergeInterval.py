'''
    LL56: Merge Sorted Intervals
'''


# nonSorted = [[2,6],[8,10],[15,18],[1,30]]
# nonSorted.sort(key=lambda x: x[0])
# print(nonSorted)    # [[1, 3], [2, 6], [8, 10], [15, 18]]


intervals = [[1,3],[2,6],[8,10],[15,18]]


def merge(intervals):

    intervals.sort(key=lambda x: x[0])

    merged = []
    
    # add the first interval to merged[]
    merged.append(intervals[0])

    for interval in intervals:
        
        print(interval)

        if merged[-1][1] < interval[0]:     # no merge, [2,6] compared to [8,10]
            
            print('no merge')
            merged.append(interval)
        else:
            print('merge', merged[-1][1], interval[1])
            merged[-1][1] = max(merged[-1][1], interval[1] )   # choose the max of "prev" (aka: merged[-1]) or the current interval

        print()

    print(merged)


merge(intervals)