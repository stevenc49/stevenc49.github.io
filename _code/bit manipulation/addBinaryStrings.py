# print( bin(4).replace("0b", "") )


a = "1010"
b = "1011"

decA = int(a, 2)
decB = int(b, 2)

print(decA, decB, decA+decB, bin(decA+decB))

res = bin( decA + decB ).replace("0b", "")

print(res)