'''
https://leetcode.com/problems/top-k-frequent-elements/solution/
https://hg.python.org/cpython/file/2.7/Lib/heapq.py#l16
https://www.youtube.com/watch?v=Gj4-8sRi7W0
'''

from collections import Counter
import heapq

nums = [1,1,1,2,2,3]

def topKFrequent1(nums, k):

    count = Counter(nums)

    return heapq.nlargest(k, count.keys(), key=count.get) 


def topKFrequent2(nums, k):

    c = Counter(nums)   # {1: 3, 2: 2, 3: 1}


    c = [(-v,k) for k,v in c.items()]    # (v,k)  [(3, 1), (2, 2), (1, 3)]
                                         # (-v,k) [(-3, 1), (-2, 2), (-1, 3)]
    
    heapq.heapify(c)

    output = []
    for i in range(k):
        item = heapq.heappop(c)
        output.append(item[1])
    
    return output


print(topKFrequent2(nums, 2))


____________


{% highlight python %}

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
    minHeap=[]
    c = Counter(nums)
    
    for n in c.values():
        
        heapq.heappush(minHeap, n)
        
        if len(minHeap)>k:
            heapq.heappop(minHeap)
    

    out = []        
    for k,v in c.items():
        if v in minHeap:
            out.append(k)
    
    return out


{% endhighlight %}
