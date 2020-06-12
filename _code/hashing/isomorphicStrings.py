

def normalize(word):

    # map[char] -> [mapped integer]
    myMap = {}
    count=0
    normalized=""
    for c in word:
        if c not in myMap:
            myMap[c] = count
            count+=1
            normalized += str(myMap[c])
        else:
            normalized += str(myMap[c])

    return normalized


print( normalize("aa") )
