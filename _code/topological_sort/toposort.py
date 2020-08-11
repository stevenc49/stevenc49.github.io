'''
    This is the basic topo sort from:
    https://www.educative.io/courses/grokking-the-coding-interview/m25rBmwLV00

    There isn't a problem on leetcode
'''


from collections import deque


def topological_sort(vertices, edges):

    inDegree = {i: 0 for i in range(vertices)}



def main():

    ans1 = topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
    print("Topological sort: " + str(ans1))
    assert( ans1==[3, 2, 0, 1] )

    # ans2 = topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])
    # print("Topological sort: " + str(ans2))
    # assert( ans2==[4, 2, 3, 0, 1])

    # ans3 = topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])
    # print("Topological sort: " + str(ans3))
    # assert( ans3==[5, 6, 3, 4, 0, 2, 1] )
    


main()