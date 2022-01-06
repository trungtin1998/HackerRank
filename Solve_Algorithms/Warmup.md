# Warmup
## Plus Minus
[Plus Minus challenge](https://www.hackerrank.com/challenges/plus-minus?isFullScreen=true)  
Python
```Python
def plusMinus(arr):
    res = {'positive': 0, 'negative': 0, 'zeros': 0}
    for i in arr:
        if i > 0:
            res['positive'] += 1
        elif i < 0:
            res['negative'] += 1
        else:
            res['zeros'] += 1
    for i in map(lambda x: x / len(arr) , res.values()):
        print("{:.6f}".format(i))
```
Javascript
```javascript
function plusMinus(arr) {
    let res = {'positive': 0, 'negative': 0, 'zeros': 0};
    arr.forEach(function(x) {
        if (x > 0) {
            res['positive'] += 1
        }
        else if (x < 0) {
            res['negative'] += 1
        }
        else {
            res['zeros'] += 1
        }
    });
    Object.keys(res).map(function(elemt) {
        console.log((res[elemt] / arr.length).toPrecision(6));
    })   
}
```
## Staircase
[Staircase challenge]()  
Python
```python
def staircase(n):
    for i in range(1, n + 1):
        print("{0:>{1}}".format('#' * i, n))
```
Javascript
```javascript
function staircase(n) {
    for (let i = 1; i <= n; i++) {
        console.log('#'.repeat(i).padStart(n))
    }
}
```
## Mini-Max Sum
[Mini-Max Sum challenge](https://www.hackerrank.com/challenges/mini-max-sum/problem)  
Python
```python
def miniMaxSum(arr):
    xmin = xmax = arr[0]
    xsum = 0
    for i in arr:
        xsum += i
        if i < xmin:
           xmin = i
        elif i > xmax:
            xmax = i
    print("{0} {1}".format(xsum - xmax, xsum - xmin))
```
Javascript
```javascript
function miniMaxSum(arr) {
    // Write your code here
    let xmin = arr[0]
    let xmax = arr[0]
    let xsum = arr[0]
    for (let i = 1; i < arr.length; i++) {
        xsum += arr[i]
        if (arr[i] < xmin) {
            xmin = arr[i]
        }
        else if (arr[i] > xmax) {
            xmax = arr[i] 
        }
    }
    console.log('%s %s', (xsum - xmax), (xsum - xmin))
}

```
## Birthday Cake Candles
[Birthday Cake Candles challenge](https://www.hackerrank.com/challenges/birthday-cake-candles/problem)  
Python
```python
def birthdayCakeCandles(candles):
    xmax = candles[0]
    xrepeat = 1
    for i in range(1, len(candles)):
        if candles[i] > xmax:
            xmax = candles[i]
            xrepeat = 1
        elif candles[i] == xmax:
            xrepeat += 1
    return xrepeat
```
Javascript
```javascript
function birthdayCakeCandles(candles) {
    let xmax = candles[0];
    let num_repeat = 1;
    for (let i = 1; i < candles.length; i++) {
        if (candles[i] > xmax) {
            xmax = candles[i];
            num_repeat = 1;
        }
        else if (candles[i] == xmax) {
            num_repeat++;
        }
    }
    return num_repeat;
}
```
## Time conversion
[Time conversion challenge](https://www.hackerrank.com/challenges/time-conversion/problem)  
Python

Javascript
