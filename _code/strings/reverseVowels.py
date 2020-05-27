import re

str = "hello"


arr = []
for i, c in enumerate(str):
    if re.search("[aeiou]", c):
        arr.append(i)

print( arr )


# for i in range(int(len(arr)/2)):

#     # swap arr[i] and arr[-i]
#     tmp = str[i]
#     str[i] = str[arr[-i]]
#     str[arr[-i]] = tmp


# print(str)