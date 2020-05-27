
bo = [

    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]

]

print( bo[1][2] )   # 1 down, 2 right

print(len(bo))
print()

print('\nprinting row')
for i in range(len(bo)-1):
    print(bo[0][i])


print('\nprinting col')
for col in range(len(bo)-1):
    print(bo[col][0])


print('\nprint both (horizontally first)')
for row in range(len(bo)):
    print(bo[row])

print('\nprint both (horizontally first, element by element)')
for row in range(len(bo)):      # horizontal first, loop over "row" first

    print(bo[row])
    for col in range(len(bo[0])):
        print(bo[row][col])

print('\nprint both (vertically first, element by element)')
for col in range(len(bo[0])):   # vertical first, loop over col first

    print("row of :" + str(bo[0][col] ) )
    for row in range(len(bo)):
        print(bo[row][col])

print('\njust gets first column using list comprehension')
print( [i[0] for i in bo] )