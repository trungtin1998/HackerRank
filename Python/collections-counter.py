# Link to chall: https://www.hackerrank.com/challenges/word-order/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
from collections import Counter

res = Counter(input() for _ in range(n))
print(len(res))
print(*res.values())
