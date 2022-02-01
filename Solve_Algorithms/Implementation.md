# Implementation
## Migratory Birds
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
