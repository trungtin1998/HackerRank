# 
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations, product
k, m = list(map(int, input().split()))
l = []
for _ in range(k):
    l.append((list(map(int, input().split()))[1:]))

mymax = 0
for x in list(product(*l)):
    tmp = (sum(i**2 for i in x)) % m
    if tmp >= mymax:
        mymax = tmp
print(mymax)
