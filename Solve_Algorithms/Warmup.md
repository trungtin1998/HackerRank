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
