

'''
    EPI; 6.1

'''



def main():

    # the input
    x = -123

    s = []

    # deal with negative case
    is_neg = False
    if x < 0:
        is_neg = True
        x = abs(x)

    # deal with the happy case
    while True:

        s.append( chr( ord('0') + x%10 ) )  # ord() returns unicode of digit, chr() returns char of unicode
        x//=10

        if x==0:
            break

    print (s)

    print ('-' + ''.join(reversed(s)) if is_neg else reversed(s))       # reversed() returns an iterator, ''.join() concontenates iterators
    # print ('-' if is_neg else '') + ''.join(reversed(s))


if __name__ == "__main__":
    main()
