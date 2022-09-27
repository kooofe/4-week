N = 4


def showMatrix(mat):
    i = None
    j = None
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end=" ")
        print('')


def kthSmallest(arr, n, K):
    arr.sort()

    return arr[K - 1]


def ReplaceDiagonal(mat, K):
    i = None
    j = None
    arr = [0] * N

    for i in range(N):
        for j in range(N):
            arr[j] = mat[i][j]
        mat[i][i] = kthSmallest(arr, N, K)
    showMatrix(mat)


mat = [[1, 2, 3, 4], [4, 2, 7, 6], [3, 5, 1, 9], [2, 4, 6, 8]]

K = 3
ReplaceDiagonal(mat, K)