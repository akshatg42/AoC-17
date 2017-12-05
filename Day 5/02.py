from sys import stdin
inp = []
for line in stdin:
    inp.append(int(line))
curr=0
steps=0
while curr<len(inp):
    steps = steps + 1
    if inp[curr] >=3:
        inp[curr] = inp[curr] - 1
        curr = curr + inp[curr] +1
    else:
        inp[curr] = inp[curr] + 1
        curr = curr + inp[curr] - 1
print(steps)