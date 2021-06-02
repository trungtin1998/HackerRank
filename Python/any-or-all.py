# Link to chall: https://www.hackerrank.com/challenges/any-or-all/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = int(input())
l = list(map(int, input().split()))

def isPalindromic(num):
    return str(num) == str(num)[::-1]

print(all(i>0 for i in l) and any(isPalindromic(i) for i in l))
