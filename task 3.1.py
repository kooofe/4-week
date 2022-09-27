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
b = "YES"
for i in range(m):
    for j in range(n):
        if a[i][j] != a[j][i]:
            b = "NO"
            break
print(b)