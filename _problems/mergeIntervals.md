---
layout: page
title:  Merge Intervals
last_solved: 2020-06-03
category: intervals
leetcode_url: https://leetcode.com/problems/merge-intervals/
status: Attempted
---

###### Problem:

Turn ```[[1,3],[2,6],[8,10],[15,18]]``` into ```[[1,6],[8,10],[15,18]]```

###### Solution:

As you're looping thru, compare the prev's interval with the current interval.

If the prev[1] > curr[0], that means there's a merge and you just replace it with the ```max(prev[1],curr[1])```

Otherwise, just append to the merged output array.

O(n*logn) time (linear time to go thru intervals, sort at beginning takes logn)
O(n) space

{% highlight python %}


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


{% endhighlight %}


![1](https://gncsea.dm.files.1drv.com/y4mjA3je8pcrbSN4OeIyS6_Fbp3CccXJ_TNvSRzIRVqPR1FqKHQBJ3Se-BkQXL8E7ERPH4epEPNYVkveF7AsUgleTVjV11zb0hwLTYRBXLoTTmLs9K2LceSew1OItMb5cinpieckIkHkbirHvvZECTMjYs_nyU4X9Xb9-TRF6fpQlwtuB5vfxnk717JiS7RNnBnG5N60a_9MJQTy7isyZ3coA?width=2790&height=1030&cropmode=none)

![2](https://gnclyq.dm.files.1drv.com/y4mo6iX6isxgelOx67T_9bxo5-kMe5dekj4FGDn3lXlqLWKfFpgZfkGoTfFX8rL9CLWJavxlnYFfEG-Utz_kqWJvAzDsr6W0bEOav2tQQ8KuQrZU3BiYrSLkGKtVcFMH6gDO3qpC1pYn0FV-_-uO8vVhyrPYRfT5wxYhlRGT0N0qjJ6kHPDGv1buTrI6vlaoxTnGxFuZ6EQ_cNqtAYAwpnN9w?width=1817&height=2183&cropmode=none)
![3](https://gnekva.dm.files.1drv.com/y4mUVOcDYT0nz9z9jc9JevipHYRKKrxZ4HPG5t4Cxb4GlGhFHuQYZxzV34nmMhw3Ogv_PAX8Z_-9aOFoU7f8N2vh27CXVpKAhkLGG4BiSZkr8TEUIfAb9HWSZXuLqjjILBErFhYYMCwqq66C_JcQkBjfw66Wqh_dXyNrZo2hnq2kaOlKj1YFr8mSmc2pfXNpcJTLceIrUIm4etzfw2cPSHXzw?width=1365&height=2974&cropmode=none)

