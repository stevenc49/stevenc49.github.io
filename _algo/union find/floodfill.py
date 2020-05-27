image = [[1,1,1],
        [1,1,0],
        [1,0,1]]


# def floodFill( image, sr, sc, newColor):
#     R, C = len(image), len(image[0])
#     color = image[sr][sc]
#     if color == newColor: return image
#     def dfs(r, c):

#         print(r,c)

#         if image[r][c] == color:
#             image[r][c] = newColor
#             if r >= 1: dfs(r-1, c)
#             if r+1 < R: dfs(r+1, c)
#             if c >= 1: dfs(r, c-1)
#             if c+1 < C: dfs(r, c+1)

#     dfs(sr, sc)
#     return image

def floodFill(image, startRow, startCol, newColor):

    R = len(image)
    C = len(image[0])
    oldColor = image[startRow][startCol]
    if oldColor == newColor: return image

    def dfs(r, c):

        # choose whether or not to advance
        # if image[r][c]==oldColor:

        print(r,c)

        if image[r][c] == oldColor:
            image[r][c] = newColor
            if r>=1: dfs(r-1, c)    # go up
            if r+1<R: dfs(r+1, c)   # go down
            if c>=1: dfs(r, c-1)    # go left
            if c+1<C: dfs(r, c+1)   # go right

    dfs(startRow, startCol) # mutates image, but doesn't return image

    return image
        


print(floodFill(image, 1,1,2))

