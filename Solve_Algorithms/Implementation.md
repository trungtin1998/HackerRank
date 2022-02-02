# Implementation
## Migratory Birds
Python
```python
def migratoryBirds(arr):
    # Write your code here
    d = {}
    for i in arr:
        if i in l.keys():
            d[i] += 1
        else:
            d[i] = 1
    return sorted(d.items(), key=lambda item: (item[1], -item[0]), reverse = True)[0][0]
```
Javascript
```js
function migratoryBirds(arr) {
    // Write your code here
    let d = {};
    let max = 0, res;
    arr.forEach(function(i) {
        d[i] == undefined ? d[i] = 1 : d[i] += 1;
        if (d[i] > max) {
            max = d[i];
            res = i;
            console.log("Max: " + max);
            console.log("Value: " + res);
        }
        else if (d[i] == max) {
            res = (i < res) ? i : res;
        }
    });
    return res;
}
```
