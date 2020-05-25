---
layout: page
title:  Longest Common Subsequence
---


```
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 
```


{% highlight python %}

str1 = "AAB"
str2 = "AZB"

def lcs(text1, text2):

    n= len(text1)
    m= len(text2)

    # creates an [m+1][n+1] matrix, filled with zeros
    table=[[0]*(n+1) for x in range(m+1)]
    
    for i in range(1, m+1):
        for j in range (1, n+1):

            # first char is the same, so add 1 to count
            if text2[i-1]==text1[j-1]:
                table[i][j]= 1+table[i-1][j-1]
            # first char is different, so break into subproblems and take the max
            else:
                table[i][j]=max(table[i-1][j],table[i][j-1])

    
    print [0]*(n+1)
    print range(m+1)
    print table
    print max(table)    # this get the last element at the end of the list
    return max(max(table))  # this gets the last element at the bottom right corner (last element of both lists)



print lcs(str1, str2)


{% endhighlight %}


![image1](https://gnfapq.dm.files.1drv.com/y4mZlth_qJCTlKJzsxVXX98_AG9IK8AYIiD6xyAEMPDfxF1FJFbE0z_rpEBOkZe0I65WDkyjiWZj3x4fGkqPjBT7ZrN1gmNos7vavy-EjgFiz6lFt3odQOYxbrxIxuCA8dEfPOcvqC2p_rKtb2nD6FGhClcL58TZMnbH2JEvsUZ2OdOWSd14TqjsqIut8vAdOWie9ZWU-J7qm_gnKrQcVv1Pg?width=1782&height=2278&cropmode=none)