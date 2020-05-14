---
layout: page
title:  Count Ones (In Array)
---

{% highlight text %}

'''
    https://leetcode.com/problems/counting-bits/

    Problem:

    Given num, return array which contains numOnes
    Ie, input = 2, return [0,1,1]

    Do it in O(n) time, and not O(n*numBits)

    Solution: dynamic programming (build table bottom up)

    d[i] = d[i//2] + (i%2)

    ex:
    d[3] = d[3//2] + 3%2
         = d[1] + 1
         = 2
    d[6] = d[6//2] + 6%2
         = d[3] + 0
         = 2 + 0
         = 2
    d[7] = d[7//2] + 7%2
         = d[3] + 1
         = 2 + 1 = 3

    https://leetcode.com/problems/counting-bits/discuss/626777/Easy-DP-Explanation-%3A-Python-Solution
'''

{% endhighlight %}


{% highlight python %}



def countOnes(num):

    if num==0: return [0]
    if num==1: return [0,1]


    dp=[0,1]

    for i in range(2, num+1):
        # dp[i] = dp[i//2] + (i%2)
        dp.append( dp[i//2] + (i%2) )

    return dp

print(countOnes(2))

{% endhighlight %}


![image1]()