---
layout: page
title:  Restore IP Addresses
last_solved: 
category: backtracking
leetcode_url: https://leetcode.com/problems/restore-ip-addresses/
status: Attempted
---

Problem
-------

```
Given a string s containing only digits. Return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single points and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "1111"
Output: ["1.1.1.1"]
Example 4:

Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
Example 5:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

Solution
----------



{% highlight python %}

    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def dfs(s, index, path, res):
            
            if index==4:
                if not s:   # why is this here?
                    res.append( path[:-1] )
                return
            
            
            
            for i in range(1,4):
                
                if i<=len(s):
                    
                    if i==1:
                        dfs(s[1:], index+1, path+s[:i]+".", res)
                    
                    elif i==2 and s[0]!="0":
                        dfs(s[i:], index+1, path+s[:i]+".", res)
                        
                    elif i==3 and s[0]!="0" and int(s[:3]) <= 255:
                        dfs(s[i:], index+1, path+s[:i]+".", res)
        
        
        res = []
        dfs(s, 0, "", res)
        return res
    

{% endhighlight %}

______________



{% highlight python %}


{% endhighlight %}

![image1]()