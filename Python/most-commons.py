# Link to chall: https://www.hackerrank.com/challenges/most-commons/problem
#!/bin/python3
## first solution
from collections import Counter

if __name__ == '__main__':
    l = [c for c in input()]
    for i in sorted(Counter(l).items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(*i)
      
## second solution: in most_common(), elements with equal counts ordered in the order first encountered that just occurs in python2, not in python3
#!/bin/python3
from collections import Counter

if __name__ == '__main__':
    for i in Counter(sorted(input())).most_common(3):
        print(*i)
