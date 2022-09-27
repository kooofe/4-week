def printArray(arr, m, n):
    for i in range(m):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()


def sortArr(arr, m, n):
    for i in range(m):
        arr[i].sort()
    print()


n = int(input('введите кол строк:'))
m = int(input('введите кол столбцов:'))
a = []
for i in range(m):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    a.append(b)

print('исходный массив')
printArray(a, m, n)

sortArr(a, m, n)
print('измененный массив')
printArray(a, m, n)
