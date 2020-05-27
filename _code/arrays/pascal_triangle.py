'''

    https://leetcode.com/problems/pascals-triangle/

'''



def main():

    def generate(numRows):

        triangle = []

        if numRows==0:
            return []

        # add first row
        triangle.append([1])

        # add other rows
        for i in range(1, numRows):

            curr_row = i

            # append placeholders to each row
            row = []
            for i in range(0, curr_row+1):

                if i==0:
                    row.append(1)
                elif i==curr_row:
                    row.append(1)
                else:
                    # print triangle[curr_row-1][i]
                    # print triangle[curr_row-1][i-1]

                    # row.append(None)
                    row.append( triangle[curr_row-1][i] + triangle[curr_row-1][i-1] )

            triangle.append(row)


        return triangle

        
    print generate(5)




if __name__ == "__main__":
    main()