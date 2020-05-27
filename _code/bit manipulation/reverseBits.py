


def reverseBits(str):

    n = int(str)

    rev = 0

    # tranverse bits from right to left
    while n>0:

        rev = rev << 1

        # if current bit is 1
        if (n&1==1):
            rev = rev ^ 1

        n = n >> 1
    
    return rev


print reverseBits("4567")


