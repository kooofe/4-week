n=3
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
def min_elts(a):
    return list(map(min,a))