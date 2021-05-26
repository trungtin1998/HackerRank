# Link to problem: https://www.hackerrank.com/challenges/maximize-it/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations, product
k, m = list(map(int, input().split()))
l = []
for _ in range(k):
    l.append((list(map(int, input().split()))[1:]))

res = set()
for x in list(product(*l)):
    res.add((sum(i**2 for i in x)) % m)
print(max(res))
