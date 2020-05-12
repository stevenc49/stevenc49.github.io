---
layout: page
title:  Is Same Tree?
---




{% highlight python %}

class TreeNode:
 
    def __init__(self, val):
 
        self.val = val
        self.left = None
        self.right = None



def isSameTree(p, q):

    if not p and not q:
        return True
    
    # both null already covered above
    if not p or not q:
        return False
    
    if p.val != q.val:
        return False
 
    leftRes = isSameTree(p.left, q.left)
    rightRes = isSameTree(p.right, q.right)

    return leftRes and rightRes


# def isSameTree(p,q):
#     if p and q:
#         return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
#     return p is q


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)


root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

p = root
q = root2

print p
print q
print isSameTree(p, q)

{% endhighlight %}


![image1](https://srk2ka.dm.files.1drv.com/y4mjDbmv7Vtxnh6G4RGcukbQFQMS77M9yp4O6b8Tvl2aC1oYemtm6Ug-E69benEJDd1KlSHea-m_CvmbQM-yuhAdgdYUaGbANgQ4x8UnBicvytnRoVECx8jxBbbSkhkhC8p_FWtPTiXWlHAu1z2rwuq7aS70iQiNABQoTM71CiVTGCWaE1Z8h8Dkl27iFhcwAOtyOiOEjGD56LWhoIpuAue_w?width=1537&height=1324&cropmode=none)
