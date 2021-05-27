# Link to chall: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
import re
res = OrderedDict()
for _ in range(int(input())):
    tmp = re.search("(.*) (\d+)", input())
    res[tmp[1]] = res.get(tmp[1], 0) + int(tmp[2])
for x,y in res.items():
    print("{} {}".format(x,y))
