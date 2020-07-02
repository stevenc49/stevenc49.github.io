
n=5

def arrangeCoins(n):
    l = 1
    h = n
    while l<=h:
        mid = l + (h-l)//2
        temp = int(mid*(mid+1)/2)

        print(l, mid, h, temp, [ (x*(x+1)//2) for x in range(l,h)])

        if temp == n:
            return mid
        if temp < n:
            l = mid + 1
        else:
            h = mid - 1
    return h
    
print(arrangeCoins(n))