n = int(input("enter the n: "))
m = int(input("enter the m: "))
a = []
print("enter the row by row")
for i in range(n):
    a.append(list(map(int, input().split())))

print('origin array: ')
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
