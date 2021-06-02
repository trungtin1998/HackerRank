# Link to chall: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
cube = lambda x: pow(x,3)# complete the lambda function 

def fibonacci(n):
    res = [0,1]
    for i in range(n - 2):
        res.append(res[i] + res[i + 1])
    return res[0:n]
    # return a list of fibonacci numbers

if __name__ == '__main__':
