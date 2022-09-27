def sortRowWise(m):
    for i in range(len(m)):

        for j in range(len(m[i])):

            for k in range(len(m[i]) - j - 1):

                if m[i][k] > m[i][k + 1]:
                    # swapping of elements
                    t = m[i][k]
                    m[i][k] = m[i][k + 1]
                    m[i][k + 1] = t

    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()


m = [[9, 8, 7, 1], [7, 3, 0, 2], [9, 5, 3, 2], [6, 3, 1, 2]]
sortRowWise(m)