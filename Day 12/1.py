from sys import stdin

def addToSet(group, data, i):
    l = len(group)
    for x in data[i]:
        group.add(x)
    if l == len(group):
        return
    for x in data[i]:
        addToSet(group, data, x)

group = set([0])
data = []
for line in stdin:
    th = line.split("<->")[1]
    data.append(list(map(int, th.split(","))))
addToSet(group, data, 0)
print(len(group))