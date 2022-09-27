n=4
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
p = 0
s = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] > 0:
            s += a[i][j]
            p+= 1

print("number of positive:",p)
print("sum:",s)