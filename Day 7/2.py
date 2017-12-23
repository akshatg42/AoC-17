from sys import stdin

def check_weight(base, mappings, weights, k):
    if len(mappings[base]) == 0:
        return k
    child_weights = {}
    temp_array = []
    for x in mappings[base]:
        child_weights[x] = calc_weight(x, mappings, weights)
        temp_array.append(child_weights[x])
    temp_array.sort()
    req = temp_array[int(len(temp_array)/2)]
    if temp_array[0] != req:
        odd_out = temp_array[0]
    else:
        odd_out = temp_array[len(temp_array)-1]
    if odd_out == req:
        return k - len(mappings[base])*req
    else:
        for x in mappings[base]:
            if child_weights[x] == odd_out:
                return check_weight(x, mappings, weights, req)


def calc_weight(base, mappings, weights):
    w = weights[base]
    for x in mappings[base]:
        w = w + calc_weight(x, mappings, weights)
    return w

Left = set()
Right = set()
mappings = {}
weights = {}
for line in stdin:
    line = line.strip()
    left = line.split("(")[0]
    weight = line.split("(")[1].split(")")[0]
    weights[left.strip()] = int(weight)
    right = line.split(")")[1].split("->")
    Left.add(left.strip())
    mappings[left.strip()] = []
    for x in right:
        x = x.split(",")
        for i in x:
            i = i.strip()
            if len(i) > 0:
                mappings[left.strip()].append(i)
                Right.add(i)
base = Left - Right
for x in base:
    print(check_weight(x, mappings, weights, 0))
