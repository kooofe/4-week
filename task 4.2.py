n=int(input('введите кол строк:'))
m=int(input('введите кол столбцов:'))
a=[]
for i in range(m):
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

a = [[1 if x>0 else 0 for x in i] for i in a]
for i in range(len(a)):
    print(*[a[i][x] if x<=i else '' for x in range(len(a[i]))],'')


