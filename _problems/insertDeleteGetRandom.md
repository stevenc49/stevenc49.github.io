---
layout: page
title:  Insert Delete GetRandom O(1)
last_solved: 2020-06-12
category: hashtable, design
leetcode_url: https://leetcode.com/problems/insert-delete-getrandom-o1
status: Solved
---

Problem
-------

```
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

```

Solution
----------

{% highlight python %}

class RandomizedSet:

    def __init__(self):
        
        self.map1 = {}
        self.map2 = {}
        self.numElements = 0

    def insert(self, num):
        
        if num not in self.map2:
            self.map2[num] = self.numElements
            self.map1[ self.numElements ] = num
            self.numElements+=1
            
            return True
        
        return False    # already present
        
    
    def remove(self, num):
        
        if num in self.map2:
            
            # remove last element
            if self.map2[num]==self.numElements-1:
                index = self.map2.pop(num)
                self.map1.pop(index)
                self.numElements-=1

            # remove but not last element
            else:

                # if we remove index, then there will be a gap
                removedIndex = self.map2.pop(num)
                self.map1.pop(removedIndex)
                self.numElements-=1
                
                # take the last element and fill the gap
                lastElement = self.map1[self.numElements]
                saveLastElementIndex = self.map2[lastElement]
                self.map2[lastElement] = removedIndex
                
                self.map1.pop(saveLastElementIndex)
                self.map1[ self.map2[lastElement] ] = lastElement
        
            return True
        
        return False    # not in set
    
    
    def getRandom(self):
        
        index = random.randrange(0, len(self.map1) )
        return self.map1[index]

{% endhighlight %}


![image1]()