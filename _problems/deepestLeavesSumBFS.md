---
layout: page
title:  Deepest Leaves Sum (BFS)
last_solved: 2020-08-31
category: bfs
leetcode_url: https://leetcode.com/problems/deepest-leaves-sum/
status: Solved
---




{% highlight python %}

    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        if not root: return 0
        
        queue = [root]
        levels = []
        
        while queue:

            level = [] 
            
            for _ in range(len(queue)):
            
                node = queue.pop(0)
            
                level.append(node.val)
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(level)
        
        return sum(levels[-1])

{% endhighlight %}


