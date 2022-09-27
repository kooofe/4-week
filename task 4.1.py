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
s=[]
for i in range(len(a)):
    s.append(sum(a[i]))
print(a[s.index(max(s))],'largest sum:',max(s),a[s.index(min(s))],'smallest sum:',min(s))
