---
layout: page
title:  Practice Log
---

### Jun 25

I just watched David V's course on "Everybody can build a Twitter Audience" and it convinced me that I need to gain credibility before I can start any entrepreneurial adventure. Since I'm already working on leetcoding, I can start small and tweet/post my leetcode solutions on medium/leetcode/twitter, etc.



### Jun 23

Need to do telus work first. Then go back to Complete Binary Tree Node problem.

I think I've successfully built the habit of leetcoding a little bit every day.

### Jun 22

Make a timeline for reaching milestones. (IE: by August, start applying to tier B companies)

Do June Challenge, then work on permutation problems. Do not spend more than 30 min figuring out a solution and not more than an hour coding it.

Another list of questions: https://docs.google.com/document/d/1wUCqhVHydWiDk6FJdFLSMpgigNrGcs4OFZg0Wa7JGEw/preview?pru=AAABcwEKa6A*jTAyJNFMW1ButNqUo_V6zA


When a problem is really hard to understand, try debugging, putting print statements or finding a solution to a similar problem.

### Jun 21

I have definately stopped consistently doing the June challenge. I should get back into the habit of doing it. It's about how you recover after getting off the wagon.




### Jun 20

I tried the weekly contest. The time pressure is there. There are also virtual contests where rank will not be affected.

When the contest is finished, you see your rank amongst other ppl. For my first one, I got 1/4 question correct with a rank of 9316/13807.




### Jun 19

Other than doing problems from a problems list, can also go thru youtube video playlists of known leetcode youtubers.

Add due dates to learn certain tasks:
- 1 night to learn dijkstra and bfs
- 1 week to learn dp


Been learning some advanced algos recently:
- Dijkstra
- Rabin Carp
- KMP substring matching

Practice whiteboard/paper space management

Do this graph problem, it has every graph algorithm below:
https://leetcode.com/problems/network-delay-time/discuss/471164/Python-DFS-BFS-Dijkstra-Bellman-Ford-Floyd-Warshall


### Jun 18

Time to do some retrospective:

-----

Doing daily problems have been slowing down the past week. Need to keep monitor burnout/stress level.

Now that I've worked on over a hundred problems on leetcode. It's time to go back and review some of the ones that I didn't get (or do some faster and more concisely)


Things that have worked:

- this journal
- this jekyll blog for easy tracking of problems
- this site doesn't actually make me review questions, but it does have my old solutions and some notes so I can reference them in similar problems
- try to gather a bunch of similar type problems and do them in batches


----


Get to the point where the skill of doing coding interviews is a science.  Create your own list of "must review" problems before an interview. Have those problems be ones that you have worked on before because you will never be able to do all the leetcode problems ever.

---




### Jun 17

Today, do cheapest flight problem (dijkstra) and leetcode daily problem (union find).

Get used to tryign out solutions and being wrong in leetcode. It's better than being wrong in the actual interview.

----------------

Try rewriting Num Islands solution more concisely from techniques learned from Surrounded Region (for x,y in neib_list) and itertools.product()
Maybe instead of going thru new problems, go thru the ones that you have done before and make sure you can write them concisely and can communicate them well.

--------------


Leetcode post for writing concise Python code:
- https://leetcode.com/discuss/general-discussion/459791/Special-data-structures-in-Python
- https://yangshun.github.io/tech-interview-handbook/landscape

Another list of leetcode questions:
- https://yangshun.github.io/tech-interview-handbook/best-practice-questions


### Jun 16

Spent the morning working on telus shit. what a waste of time.

Today, I went thru the BFS and Dijkstra chapters in Grokking Algorithms book. It does a very good job at explaining for visual learners. Tmr will attempt some dijkstra problems.



### Jun 15


Today, I spent most of the day with the Cheapest Flight problem. I didn't quite get it even after looking at the code so tomorrow, I will focus on understand Dijkstra at a deep level before going back to the problem.

Check groking algorithms ebook for dijkstra chapter.
Can also read "competitive programming" ebook.


-----------------

I read somewhere that Leetcoding is like going to the gym for your coding skills. It's a slow marathon. That falls in line with my experience that you can't cram for an interview. I will just have to incorporate it into my daily routine or work routine.

Since you value your time, your 9-5 is when you should be leetcoding. Treat it like a job and don't bother leetcoding outside office hours.



### Jun 12

Start using interview.io sandbox to practice, they have Python autocomplete and executes code on save. (Much nicer than VS Code).




### Jun 11

Just finished the practice interview. I got this question in the interview:
https://leetcode.com/discuss/interview-question/368038/Amazon-or-Onsite-or-Group-Isomorphic-Strings




It went okay. I surprised myself when I actually came up with a solution myself in the allotted time, even though it wasn't optimal. For your practice, allocate some time to problems where you just figure it out yourself and don't stop unless you've tried for over an hour. Probably best done in some of the easier types of questions (ie: arrays, strings, hashmap).



Some other feedback has been left here:
https://start.interviewing.io/feedback/J2aykIDapnWN

Key points were:
- ask clarifying questions
- always review space and time complexity (i got space complexity wrong)


In every interview, you will always feel unprepared and you will even stress out DURING the interview. You will want to give up. Need to find some way to handle the stress and keep tackling the problem.


--------------------

Have a practice interview today at 3pm.  Should start practicing using the online environment:
https://start.interviewing.io/interview/playground?tutorial=true


It also helps you with your walk-thru dry debugging.  When you're doing a dry walk-thru online, type out the array in its current state along with all tracker variables. For example:

```
    # 2 0 2 1 1 0    i=0    s=0    e=5
    # 0 0 2 1 1 2    i=1    s=0    e=4
```

When you run the code, you can print(num, trackerVars...) at the end of the loop and verify what you get when you execute matches what you think you should get.

Getting prep'ed for my practice interview. Just reviewing all the different "bag of tricks" by going thru jekyll blog.
I should make my own list of problems to "review before an interview". Should be a handful of problems that I can review in a short amount of time.

After your interview, you should go and find it in the showcase and see where you can improve. So give it all you got.


### Jun 10


Search Insert Position
----------------------

I did the problem "Search INsert Position" all by myself. It was an easy binary search question, but it's usually one of the ones that I always failed at.

I started with what I know about binary search and modified it by thinking of all the edge cases and eventually wound up at an acceptable solution.

Looking back at some of the LC discussions, I may have over-complicated it and wrote more than I need to. The classical binary search would have suffice with a single line modification (return left if none found).

I posted my solution in the discussions for feedback.



Validate Sudoku
----------------------

Also did validate sudoku problem. I did it within a reasonable amount of time. The debugger helped with finding bugs such as ignoring ".".
It wasn't a logic problem.  Just a trivial mistake.


Rotate Image
-----------------------

Transpose and Flip. This is the second time that I'm seeing this and I really worked hard to understand it the first time.

The second time, I was able to:
- recall "the solution"
- code up the solution and get the array indexes and loop ranges correct (things I usually mess up on)

It turns out these problems are actually easier if you solve them a few times before. So it really is all just about practice and not purely talent.

------------------


Did the Hackerrank Data Engineer BS assessment yesterday. It was pretty BS. It's a good reminder that these algo questions are the easiest way to go if you get good at them.

P.S. need to categorize binary search as its own categories and practice a bunch of those questions, just like strings




### Jun 7

Booked a peer interview for Thursday @ 3pm. Should start watching other interviews from the showcase.
https://start.interviewing.io/showcase

-----------------

Teck mining company, who has no business giving technical interviews, are also giving out hacker ranks assessments now.
This whole industry has gone to shit.


### Jun 6

Goal: finish easy collection by wednesday.

Get to the point where you can read solution and understand/code it. If you don't get a solution, keep using other resources until you can understand it. You will eventually reach a eureka moment.

At least be able to comment on the code. Just find the systematic approach to get the best bang for your buck for each hour of studying.

Don't compare your ability with anyone else, just compare to your past self.



### Jun 5

Did the problem "Plus One" all by myself without reference. Sure, I took a bit longer with some corner cases but it's definately a confidence booster.

-------------

Use the Python debugger in VS Code. F5 to debug, F10 to step over.

------------

Going thru some of the SQL problems in preparation for the SQL online assessment. I'm realizin it's not just about knowing algorithms. Getting good at interviews is just about getting good at the skill of being tested.  It's not about being a good engineer and completing projects, it's about being good at leetcode problems and hackerrank shit.

https://www.hackerrank.com/dashboard

------------

Spent longer than I should have on Longest Common Prefix. It should've been an easy String problem but I'm not familiar with the basic String functions (ie: index() vs find()).

I need to spend more time on String problems too. Thinking they're too easy and avoiding them is a mistake.


-------------

Leetcoding is now full-time job. Business ideas/Real Estate are side hustles. No time for real work.

If you can't understand a problem. Try to understand as much of it and revisit it the next day. Mark it down as "Attempted" in the Solved Problems page.

After a while, you should go back and "revisit" all the ones you marked as Attempted.

Don't get stuck on any one problem. Your goal is to move ahead and do as many problems as possible with deliberate practice.


### Jun 4

I'm starting to realize there's no way I'm going to memorize the solution to all these problems. But I'm starting to feel like it's actually possible to "recite" these solutions in an interview if I do enough of them. It's just going to take a lot of time and practice.

So I would still have to spend all my available time on it for a chance to get lucky in an interview. Still, it's something that I should do if I have a pointless job. But I should still work on other stuff in life if I can make the time for it.



### Jun 3

I studied one new type of problem (two city scheduling). It's a greedy problem that I probably wouldn't have encountered but I did it because it was the June challenge.

That also brought me to redo (Merge Intervals) because of the foreign Python syntax to sort by first element. I need to practice python fundamentals instead of doing my Java style habits.

Python practices here:
- https://www.hackerrank.com/domains/python
- https://learnxinyminutes.com/docs/python/



### Jun 2

Today I've done 6 problems. 5 were easy and 1 (reversing integer), I had to analyze how they handled overflow.

Something that I'm realizing is that even if I have a bunch of easy questions, it still takes a long time to do a bunch of them. And the "harder" questions could be solved in the same amount of time if you've memorized them.

Your willpower to keep doing another easy question will also be drained. At most, you might be able to get through 5-6 easy problems per day.

So the only way to do good on interviews is to do a bunch of problems, memorize them and find ways to practice more problems right before your interview.

Also, read this:
https://leetcode.com/explore/interview/card/coding-interview-strategy



-----------

Also found this other youtube channel for coding interviews:
https://www.youtube.com/channel/UCpLC2ohmappF2iUsWYRnsxg

So we have "Terrible Whiteboard", nick white and backtobackswe.



### Jun 1

Doing the list Leetcode Top Interview Questions Easy List:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/

Just want to see if I can do all the easy ones now that I had 3 months to practice.



### May 30

Made a python script that generates "Solved Problems" listed by last modified date. Hopefully this will help with space repetition.



### May 29

Studied
- Set Matrix Zeros

I attempted Set Matrix Zeros but ran into gotcha. When you modify the matrix in place, it will screw over teh zeroing logic. This is like a gotcha that I found when validating BST.  It seems pretty simple but there's a gotcha.  The only way is to just do this algorithms and remember the gotchas.

I swear these problems really make you feel stupid and the only way to overcome them is to play the stupid game and memorize the problems and solutions.



### May 28

Reviewed:
- num islands

Found [this](https://leetcode.com/discuss/general-discussion/655708/graph-problems-for-beginners-practice-problems-and-sample-solutions) great list of graph problems.

Use the forest app to focus and not get distracted. Remember, leetcode first priority, shopify is a side hustle.

### May 27

Review:
- search matrix

Studied:
- Water with most water
- house robber 2

Today, I did a brand new problem "Water with Most water". I jumped straight to the solution, read the optimum approach and was able to code up the solution myself within 25 min.


- The more I'm working on leetcoding/app dev/spending time with loved ones, the more i'm realizing that time management is key.
- Think of leetcoding as full time job and dropshipping/app development as side hustle
- I think last time I wasted time on Project Euler and UVA Online Judge but they were not tailered towards interviewing enough.

### May 26

Reviewed:
- house robber
- max sub array


I just reviewed house robber and max sub array today. Seems like even if I think I know the appraoch, there's lots of things coding-wise that trip me up. Definately need to review old problems from time to time.


Also, I only have a certain level of WILLPOWER everyday. It's best to split it between working on my business and leetcode. But I cannot neglect either one.


Todo:
matrix binary search:
https://www.youtube.com/watch?v=41ON2EghJi0

Try geometric problems:
https://leetcode.com/problems/generate-random-point-in-a-circle
https://www.youtube.com/watch?v=pvimAM_SLic


I swear memorizing these intereview problems is as dumb as memorizing prayers when I was a kid.


### May 25

Reviewed
- Longest Common Subsequence (25 min to reviewed approach, another 30 to code with minor mistakes)

### May 22

Reviewed
- Merge Sorted List (Iterative)
- Reverse LL (Iter)

Back from a 2-day break. Been thinking entrepreneurally since was getting burnt out from leetcoding.
I should balance out business and leetcode.

Tips for leetcoding:
- Use Forest app for timeboxing leetcode.
- Use space repetition to rework old problems in leetcode.


Other ideas:
- keep track of submission by problems
- track myshopify stores and copy products


### May 19

Studied
- Coin Change
- House Robber

Just looked at solutions and memorized/learned from them. Will review in a few days.


### May 16

Tomorrow or next week, need to review a few problems that I've "forgotten"
- Find Min in Sorted Array
- missing number
- reverse bits
- remove nth node from end of list



### May 15

Studied
- flood fill / num islands


Just finished studying the Flood Fill problem. I think I found a pattern/routine that works.

1) Find a new problem.

2) Understand the problem and think of initial solution for 5 minutes.

3) Look at discussion solutions

4) Implement the discussion solutions yourself without looking (you'll catch some small errors)

5) Redo problem a few days later.



### May 14

Studied (new problem or new algo)
- longest substring without repeating chars
- count ones in array

Reviewed
- numOnes
- merge sorted linked lists (recursive)


Tip from Nick White:  don’t sit there and try and solve it. Just look at the solutions and learn
Let's see how many new problems I can "study" using this method. I can always go back to "review" the problems.
Quantity over Quality! FTW

Once you learn it, write it down in notes (ie: blog) and keep looking over it. Who cares if you're "memoroziing it". Just do whatever works.

Found this article on bit manipulation:
https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently/207733/



Looking at a new algorithm (union find), from problem "number of islands". Time to add this to your "algo toolbelt"
https://leetcode.com/problems/number-of-islands/discuss/583483/Summarize-of-3-Types-of-solution-methods
Do these next:
- https://leetcode.com/problems/flood-fill/
- https://leetcode.com/problems/number-of-islands/

Found a backtracking algo:
https://www.thecshandbook.com/Backtracking

Leetcoding is starting to become fun. Considering the alternative is doing telus work. Both type of work is pointless but there's at least a greater chance of being rewarded with leetcode.


### May 13

Studied
- merge intervals


Reviewed
- reverse linked list (iterative)
- link list cycle (hashmap and floyd)

Today, had a lack of motivation. Did a new hard problem instead (merge intervals).
Should do 1-2 "hard" problems that will require studying and "review" the rest.

Also found out about https://interviewing.io/. It's free so try it out when you're more comfortable.





### May 12

today is pop quiz time

- BFS
- buy and sell stock
- deepest leaves sum (dfs)
- same tree
- symmetric tree
- invert tree
- validate bst (studied)

keep track of which problem is "studied" vs "reviewed"


### May 6

- Max Subarray
- Max Product Subarray

Having problem with product subarray, will do a dry run later
https://stackoverflow.com/questions/19148539/getting-range-of-max-product-subarray-using-kadanes-algorithm

Getting good at leetcode article:
https://heidi-newton.com/blog/getting-good-at-leetcode



### May 5

Setup algo blog at stevenc49.github.io to keep track of blind 100 curated questions and keep solutions to problems.

Also found out about https://learnxinyminutes.com/docs/python/



### May 1

- LCA binary tree
- symmetric tree

I am definately getting better at solving and reasoning thru tree problems. Sometimes you just need to work on other types of problems and come back to them later.

use multiple resources while studying answers:
- youtube
- LC discussions
- EPI

Goal right now is to try to understand and do as many questions as possible per day (increase learning rate)
Trying to take frequent breaks (playing / watching games between questions)

from blind:
"I'll give you a hint on career success: politics and expectations management."
"SAT tests get you into a good college, whiteboard tests get you a good job. Unfortunately that’s just how things work today"
Ref: https://www.teamblind.com/post/To-all-the-good-students-who-are-now-good-at-Leetcode-EraCXo5R


### Apr 30

- rotate matrix
- is tree balanced
- search sorted matrix


rotate matrix is turning into one of the more interesting and one of my fav problems, since transposing/flipping and for loop arguments are non-trivial

for array problems, stick to medium difficulty problems


### Apr 29
- validate sudoku box (validate box can be reduced to 1-d array with formula k = (i//3) * 3 + (j//3)
- spiral matrix
- rotate matrix (transpose and flip method) https://www.youtube.com/watch?v=SA867FvqHrM



watched nick white youtube on how he got into google: https://www.youtube.com/watch?v=nmf-oObylnk
- he said he grind pramp interviews, 8 per day for a month
- try to solve medium problems
- found a python concept tutorial list - https://www.hackerrank.com/domains/python


### Apr 29

- merge-two-sorted-lists (took a little more than an hour and had to rework it for edge cases) (ie: empty list)
- merge two sorted list recursive

Revisit Later:



### Apr 27

- group anagrams (solved in 15 minutes)

also can work on problems from app "Data Structures & Algorithms"


### Apr 24

- binary search
- 

yesterday, i couldn't even write a binary search. it's embarassing for a software engineer. i need to get to a level that even i would approve of.

do quantity practice over quality, do as many varied types of questions and just look over solutions

try to replicate solving after even are seen

maybe make a space repetition app to redo problems that you were struggling with:

ie: had trouble doing "find min in sorted array but eventually understood the solution, next couple days, come back to it and redo it"

it's good to take a break and reflect on how you can improve your practice. today, after finishing binary search and search min in sorted array, i reflected on how i can "remember" these solutions and the idea of spaced repetition came in

also useful to reflect on problems that you wanted to solve, understood but didn't and want to retry

P.S. officially today, i've been practicing consistently for 3 weeks



### Apr 23

Retrospective
---------------
The goods / What has been working:
- stop working on Telus work and only focus on interviewing
- having a system / scheduled time / routine to work on it is key (get more hours in)
- posting to blog kinda helps
- journaling definately helps
- make studying convenient by making it easy to solve simple problems while watching TV

The Bads / What I need to work on
------------
- In addition to leetcoding questions, also need to:
	- know python trivial concepts (list comprehension, lambda)
	- geekforgeek problems (min and missing #) (not in leetcode)
	- system design problems
	- regex
- Need to know many different ways to solve problem
	- recursion vs iteration
	- xor in array/math problems
	- different data structures/ time vs space complexicity
- keep log book and have a list of key interview problems to do before an interview (organized way to do long term studying)

Takeaways
-------------
- Don't complain about work
- Keep the leetcoding momentum going and refine study methods after this one bad interview
- Can think about introducing system for new goal (Chinese, Business, Cooking)






### Apr 22

I bombed the 1 hr coding interview at Softmax Data.

some questions were:
1) ways to reverse string (iterative, swap, recursive)
2) are two strings anagrams
2) [ i/2 if i>3 else 0]
3) lambda function to increase every elem in array
4 regex "vowels" | "come" 
5) fib(3) giving [0,1,1]
6) 
a = [6, 5, 4, 2, 6]
1 . continuous integers randomly sorted
2. min, max
3. missing -> 3
4. duplicate -> 6

#### Takeaways

- need to stop doing telus work and only focus on interviewing
- practice python syntax/concepts as well as algorithms





### Apr 21

Merge 2 sorted list is suppose to be easy but it's hard, come back to it later


#### Cramming Retrospective:

#### Good Parts
- you can get in the mindset of it and it will boost confidence

#### Bad Parts
- you'll forget how you solved a problem a week later
- Need to keep these skills sharp for lifetime and practice regularly.
- It's not possible to cram the learning into a few days or a week



### Apr 20

Studying in on hyperdrive now that I have a coding interview in 2 days.

I actually solved the hamming distance problem by myself (bitwise problem).  new achivement


https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-100-LeetCode-Questions-to-Save-Your-Time-OaM1orEU


### Apr 15

- LCS
- BFS

Completely wrote a working BFS from scratch by myself.  I have it memorized and ingrained from thinking about it for so long.  Need to get as familiar as this with other classic problems (ie: longest common subsequence). Despite how non-intuitive it is.

got a bit complicated when i had to start keeping track of levels.  apparently the technique i used to keep track is the same technique i used in java 4 years ago, it's just much more verbose.  fuck java

---

The language matters, python has list comprehension which will make writing out the algo easier/faster.


### Apr 14

- longest common subsequence (DP)

If you need data to flow up, need to make use of return value.  And usually post order (after null check)

Just watched the LCS solution [here](https://www.youtube.com/watch?v=ASoaQq66foQ).  Will implement tmr.

### Apr 13

- deepest leaves sum (LC1302) (solve time about 1 hour with help)
- spent afternoon trying to figure out wrong error problem on sum even grandparents problem

Compare your python solution to [this](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/discuss/562939/Simple-recursive-python-solution) solution tomorrow.

find out why making it postorder instead of preorder made it work.


Work days should consist of 1-2 hours of applying to jobs, and 3-4 hours of leetcoding.

Leetcoding should focus on quantity vs quality so you can identify patterns. Don't be afraid to look up solutions.  Like studying for linear algebra exam.

Ultimate goal is to get comfortable with classic questions in the shortest amount of time.

Looked at some solutions on leetcode and found some python best practices and shorcuts to make code look more clean.

An idea I got from a leetcode article is to start recording practice time in a spreadsheet like in [here](https://leetcode.com/discuss/general-discussion/571805/600-problems-in-one-year).

The columns are:
- problem topic
- problem difficulty
- time to find a solution
- time for implementation
- status (solved, not solved, solved with hints


### Apr 9

- missingNumber (XOR solution)
- twoSum ( O(n^2 solution)
- LC #1290 - binary to dec, linked list

I feel like the daily practice is showing some signs of improvement.  I just attempted the twoSum problem (which is suppose to be a super easy problem), and I was able to get the Python solution on the first try.  4 years ago, I attempted the Java solution and got a wrong ansewr.

I also intuitively understood the XOR solution for the missing numbers problem.

Did the binary to integer linked list problem.  It's an easy problem that made me think of fundamental binary properties and I had some small coding errors.  But I was able to do it in about an hour.  Not great but it's still in an afternoon.  P.S.  I checked the forums after I thought my initial process was non-ideal (using library methods).


Also read some reddit comments about leetcoding.  TDLR: leetcode or die.



### Apr 8

Did leetcode #268: Missing number.

If it's an easy one, try to get it right and compilable on the first try.  I did not because I made a small mistake, the for range loop is exclusive of the final number.  It screwed up my calculations.

My new strategy now is to sort leet codes by acceptance and tags (ie: arrays, hash tables, trees, etc)

Just reviewed the solution for missing number and encountered the XOR solution.  I still don't fully understand it intuitively but it's good to review other solutions and learn something new.

I'm feeling much more comfortable about doing these everyday.  Maybe I won't feel comfortable going for an interview tmr but I am able to work on these regularly now.  I've started building up that habit and ignoring Telus.



### Apr 7

Uploaded [Reverse Linked Listed Iterative Method](https://bubblesortblog.wordpress.com/2020/04/08/reverse-linked-list-iterative-method/) 

If it's pointer heavy with lots of iterations, it's better to draw it out and redraw each iteration.


### Apr 6

Just do lots of problems, easy or not.

Do Reverse linked list today.  You're bound to run into "end of list error"

Need to also be able to do easy questions when feeling tired.

### Apr 5

I was going entering some of my solutions into leetcode, specificailly the valid parenthesis problem and I realized my solution is just entirely wrong and does not solve the min stack problem correctly.

It doesn't even give the correct solution for "(]". My solution gives true and the answer is obviously false but I didn't see it.
I need to read the question more closely.  Entering these into leetcode will help me know what to test for.



### Apr 3

New strategy - do lots of problems, quantity over quality

I've forgotten the general solution to problems I've done exactly a week ago.  Need to review bubblesort.blog periodically.

Let's do LRU question today.
Been doing the LRU question and creating a doubly linked list.  I definatley need to work on managinging my double pointers without having to check with the compiler and running it.

In a doubly linked list, always keep track of head and tail pointers
I managed to keep track of head and tail nodes after realizing I forgotten about them but it took me a lot of time.  And I still didn't get to work on the eviction policy.

### Apr 2

- max depth of binary tree
- is tree balaned

After checking on the deepest node code, I should do this easy balanced binary tree checker question:

- https://leetcode.com/problems/balanced-binary-tree/
- https://leetcode.com/problems/maximum-depth-of-binary-tree/

I'm not sure why [this](https://leetcode.com/submissions/detail/318802426/) submission failed, but [this](https://leetcode.com/submissions/detail/318803393/) one passed.

Some tipes from reading interviewing articles:
"I found that it is extremely helpful for me to read solutions before attempting to solve the problems all by myself. "

-------------

I also just did the isTreeBalanced() problem but I really just rewrote a java solution that i rewrote 4 years ago.
I will need to actually drill down and run it step by step to really understand it and fully grasp it.


### Apr 1

I inputted the deepest node code into leetcode but I'm getting wrong answer.  I'll have to look into this.



### Mar 31

- [Print Nodes K Distance from Root](https://bubblesortblog.wordpress.com/2020/03/31/print-k-distance-from-root/)
- [Deepest Node/Get Height of Tree](https://bubblesortblog.wordpress.com/2020/03/31/get-deepest-node-get-height-of-binary-tree/)

Tried the k distance from tree node problem.  It involves a hashtable to go up the tree.  I watched Back2BackSWE video but it doesn't make sense without code.

So I'm going to try a simpler version first where we get nodes at k distance from the root.
https://www.geeksforgeeks.org/print-nodes-at-k-distance-from-root/

------

I did the deepest node by myself and got it right after some debugging.  Next time will work on leftmost deepest node.




### Mar 27

- LCA of binary tree
- serialize/deserilize binary tree

Today, I've added a blog post on LCA of binary tree nodes (without parent pointers or BST)

For the next few days, I should try out the other similar problems:

- 10.3) LCA of binary tree (done)
- 10.4) LCA with parent pointers
- 15.4) LCA of BST

Also watched a video on serializing/deserilizing a binary tree on Back2BackSWE.  Will try to implement this.

Today, I actually implemented serialize and deserialize binary tree:

- [Serialize Binary Tree](https://bubblesortblog.wordpress.com/2020/03/27/serializing-a-binary-tree/)
- [Deserialize Binary Tree](https://bubblesortblog.wordpress.com/2020/03/28/deserialize-tree/)

### Mar 26

- validate sudoku
- LCA of binary tree nodes


Yesterday, I spent so much time trying to understand the sudoku solver.  I think I should take a break from it.  Maybe implement a sudoku validator first.  The video from [Tech with Time](https://www.youtube.com/watch?v=lK4N8E6uNr4&list=TLPQMjUwMzIwMjBh1WFA0aDQLg&index=1) is actually very useful.  

What I did learn was the x,y coordinate with col,row intuition.

Did LCA of binary tree node.  Best explaination was from BackToBackSWE [here](https://www.youtube.com/watch?v=py3R23aAPCA).
The insight from this video is **"when dealing with tree recursion problems, always think of it from the point of view of a single node"**


### Mar 25

- sudoku solver

My goal today is to solve the sudoku problem with backtracking.

It's 2:30pm and I'm not making a lot of head way into this sudoku backtracking problem.  Maybe I'll work on an easier tree problem for the rest of today.
This sudoku problem is helping me get 2d rays with row and columns straight though.

[This](https://www.youtube.com/watch?v=lK4N8E6uNr4&list=TLPQMjUwMzIwMjBh1WFA0aDQLg&index=1) guy does a good job at explaining how to implement a sudoku solver.


### Mar 24

Today, I tried implementing the solution for Min Stack and I wrote a blog post for it [here](https://bubblesortblog.wordpress.com/2020/03/24/min-stack/)

Writing the blog post is really just as hard because you will have to communicate clearly to the reader your logic.  You'll also need to provide an example test scenario.

This is a good practice for communicating to the interviewer and I should do this with every problem I solve.  I should get to the point where I can communicate the problem like this guy [here](https://www.youtube.com/watch?v=nGwn8_-6e7w).

As a side note, the explaination in EPI is exactly to what the BacktoBackSWE guy describes.  So I should probably understand the solution before checking with EPI for the "cononical" solution.

The good news is that I'm building up the habit of practicing algorithms every day now.  I should keep it up and pick another problem to work tmr.

I definately need to give studying algorithms as much attention as I've given work and studying investing as in the past.  The key to this might be continous deliverate practice.

I need to remember that habit + deliberate practice = Mastery.

Same thing for Chinese.


### Mar 23

- Valid Parenthesis
- Min Stack

Solved Valid Parenthesis Problem by myself.  My solution is posted on my new blog [here](https://bubblesortblog.wordpress.com/2020/03/23/64/).
However, the solution I came up with involves 3 stacks, each keeping track of a type of brace.

This can be improved with a single stack and detecing if it's an opening or closing brace.  If it's an opening brace, we push to the stack, and if it's a closing brace, we pop from the stack.  Try this solution tomorrow.

Today, we will try to get another problem in.

I also found this great youtube channel with a teaching style that I like:
[Back to Back SWE](https://www.youtube.com/channel/UCmJz2DV1a3yfgrR7GqRtUUA/videos)

Next question that I will attempt is the Min Stack problem. The min stack problem will run into the problem when you pop from a stack and you have to update the global minimum, the solution is to store the global minimum for each element in the stack.  We can use another structure to do that, like another stack.

This solution is outlined [here](https://www.youtube.com/watch?v=nGwn8_-6e7w)




### Mar 20

- found [Techinical Interview Handbook](https://yangshun.github.io/tech-interview-handbook/best-practice-questions)
- read groking algorithms - chapter 3 recursion



### Mar 9
- reverse string using recursion
- reversed stack using recursion