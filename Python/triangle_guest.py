# Link to chall: https://www.hackerrank.com/challenges/python-quest-1/problem
# Can't use string manipulation or more than 2 loops, therefore: `print(i*"{}".format(i))` not accepted
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i * pow(10,i)//9)
