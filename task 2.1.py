n=3
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
def magsquare(a):
    n = 3
    diag1 = 0
    diag2 = 0
    for i in range(n):
        diag1 += a[i][i]
        diag2 += a[i][n - i - 1]
    if not (diag1 == diag2):
        return False
    for i in range(n):
        rows = 0
        cols = 0
        for j in range(n):
            rows  += a[i][j]
            cols += a[j][i]
        if not (rows  == cols == diag1):
            return False

    return True

if (magsquare(a)):
    print("Magic Square")
else:
    print("Not a magic Square")
