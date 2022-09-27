n=int(input('введите кол строк:'))
m=int(input('введите кол столбцов:'))
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)

print('исходный массив')
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
for i in range(n):
    tmp = a[i][0]
    a[i][0] = a[i][m-1]
    a[i][m-1] = tmp

for i in range(n):
    for j in range(m):
        print("%2d " % a[i][j], end=' ')
    print()