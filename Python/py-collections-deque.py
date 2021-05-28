# Link to chall: https://www.hackerrank.com/challenges/py-collections-deque/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
res = deque()
for _ in range(n):
    tmp = list(map(str, input().split()))
    if tmp[0] == "append":
        res.append(int(tmp[1]))
    elif tmp[0] == "appendleft":
        res.appendleft(int(tmp[1]))
    elif tmp[0] == "pop":
        res.pop()
    elif tmp[0] == "popleft":
        res.popleft()

print(*res)
