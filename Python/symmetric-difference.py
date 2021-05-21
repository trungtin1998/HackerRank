# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = set(input().split())

n = int(input())
b = set(input().split())

res = a.difference(b).union(b.difference(a))
for i in sorted(res, key = int):
    print(i)
