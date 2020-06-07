people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# turn to [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

def reconstructQueue(people):

    print(people)

    # sort ppl by decending height first and k second
    people.sort(key=lambda x: (-x[0], x[1]))

    print(people)

    ans = []
    for person, num in people:

        if num >= len(ans):
            ans.append([person, num])
        else:
            ans.insert(num, [person, num])
    return ans

print( reconstructQueue(people) )