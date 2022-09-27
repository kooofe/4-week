def smallestInRow(mat):
    minm = min(mat)
    return minm


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
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
minm = []
for i in range(n):
    minm.append(smallestInRow(a[i]))
print(minm)

for i in range(len(minm)):
        if minm[i]%2==0:
            minm[i]=0
        else:
            minm[i]=1
print(minm)