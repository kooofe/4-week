n = int(input("enter the n: "))
m = int(input("enter the m: "))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
def min_elts(a):
    return list(map(min,a))
