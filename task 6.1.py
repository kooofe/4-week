MAX = 100


def smallestInRow(mat, n, m):
    print("{", end="")
    for i in range(n):

        min = mat[i][0]

        for j in range(1, m, 1):

            if (mat[i][j] < min):
                min = mat[i][j]

        print(min, end=",")

    print("}")


def smallestInCol(mat, n, m):
    print("{", end="")
    for i in range(m):

        min = mat[0][i]

        for j in range(1, n, 1):

            if mat[j][i] < min:
                min = mat[j][i]

        print(min, end=",")

    print("}")

n = 3
m = 3
mat = [[2, 1, 7],
       [3, 7, 2],
       [5, 4, 9]];

print("Minimum element of each row is",
      end=" ")
smallestInRow(mat, n, m)

print("Minimum element of each column is",
          end=" ")
smallestInCol(mat, n, m)