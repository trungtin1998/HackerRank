# Link to chall: https://www.hackerrank.com/challenges/piling-up/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

for _ in range(int(input())):
    _ = int()input())
    d = deque(list(map(int, input().split())))
    flag = 1
    for i in reversed(sorted(d)):
        if i == d[-1]:
            d.pop()
        elif i == d[0]:
            d.popleft()
        else:
            print("No")
            flag = 0
            break
    if flag == 1:
        print("Yes")
# Another solution uses for/else structure instead of using flag paramater
