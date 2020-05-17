---
layout: page
title:  Climbing Stairs
---

Basically just fib but start dp array at [1,1]

n=3
[1, 1, 2, 3]

{% highlight python %}

def climbStairs(self, n: int) -> int:
    
    dp = [1,1]
    
    for i in range(2, n+1):
        dp.append(dp[i-1]+dp[i-2])
    
    print(dp)
    
    return dp[n]

{% endhighlight %}



![image1](https://gndbsg.dm.files.1drv.com/y4mxURBADYcPSgB7iiPXin_y8EP4Ne6SnaivuuMy0d2fjbl65EQUWxCKmc4P2GjfthE1Fxh4jy4sblxQ0UyMvH2NKTGNZez-2b4ZazYT28ksKM-xByG-GLQYx0pmZUSMjd825h3auNWJ8qh17Bw09HHbqT3WPtV2FIuM2pS-ZjYVMBk39inqkBlPaVGybJSO881FWiRbcaVUhPw94fAkN6lHA?width=1523&height=960&cropmode=none)