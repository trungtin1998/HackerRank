# Enter your code here. Read input from STDIN. Print output to STDOUT
# omega is  sample space
# res is number of cases at least one of the  indices selected contains the letter:'a'. I find the complement of result
from itertools import combinations
n = int(input())
l = list(map(str, input().split()))
k = int(input())

omega = len(list(combinations(l, k)))
m = n - ''.join(l).count('a')
res = len(list(combinations(m*'a', k)))
print("%.4f" % (1 - res / omega))
