#!/usr/bin/env python
nestedlist = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    nestedlist.append([name, score])

for i in nestedlist:
    nestedlist.sort(key = lambda x: x[1])

res = []
min_num = nestedlist[0][1]
l = len(nestedlist)
for i in range(l):
    if nestedlist[i][1] != min_num:
        secondLowest = nestedlist[i][1]
        for j in range(i, l):
            if nestedlist[j][1] == secondLowest:
                res.append(nestedlist[j][0])
        break

res.sort(key = lambda x: x[0])
for i in res:
    print i
