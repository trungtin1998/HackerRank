# Link to chall: https://www.hackerrank.com/challenges/input/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = map(int, input().split())
print(eval(input().replace('x', str(x))) == k)
