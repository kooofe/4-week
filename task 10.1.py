def maxelement(arr):
    no_of_rows = len(arr)
    no_of_column = len(arr[0])

    for i in range(no_of_rows):

        max1 = 0
        for j in range(no_of_column):
            if arr[i][j] > max1:
                max1 = arr[i][j]

        print(max1)


arr = [[3, 4, 1, 8],
       [1, 4, 9, 11],
       [76, 34, 21, 1],
       [2, 1, 4, 5]]

maxelement(arr)