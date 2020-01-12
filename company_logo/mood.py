import sys
happiness = 0
lines = sys.stdin.readline()
n = lines.split()[0]
m = lines.split()[1]
lines = sys.stdin.readline()
arr = lines.split()
lines = sys.stdin.readline()
a = {''}
for el in lines.split():
    a.add(el)
lines = sys.stdin.readline()
b = {''}
for el in lines.split():
    b.add(el)
for i in range(int(n)):
    if arr[i] in a:
        happiness += 1
    if arr[i] in b:
        happiness -= 1
print(happiness)
