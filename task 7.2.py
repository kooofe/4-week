def diagonal(A):
    N = 3

    for col in range(N):

        startcol = col
        startrow = 0

        while (startcol >= 0 and
               startrow < N):
            print(A[startrow][startcol], end=" ")

            startcol -= 1
            startrow += 1

        print()

    for row in range(1, N):
        startrow = row
        startcol = N - 1

        while (startrow < N and
               startcol >= 0):
            print(A[startrow][startcol],
                  end=" ")

            startcol -= 1
            startrow += 1

        print()


A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

diagonal(A)