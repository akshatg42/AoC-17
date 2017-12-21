import copy

def distance(pos):
    dist = 0
    while pos['x'] != 0 or pos['y'] != 0:
        if pos['x'] != 0 and pos['y'] != 0:
            if pos['x'] > 0:
                pos['x'] = pos['x'] - 1
            else:
                pos['x'] = pos['x'] + 1
            if pos['y'] > 0:
                pos['y'] = pos['y'] - 1
            else:
                pos['y'] = pos['y'] + 1
            dist = dist + 1
        else:
            if pos['x'] == 0:
                if pos['y'] > 0:
                    pos['y'] = pos['y'] - 2
                else:
                    pos['y'] = pos['y'] + 2
            else:
                if pos['x'] > 0:
                    pos['x'] = pos['x'] - 2
                else:
                    pos['x'] = pos['x'] + 2
            dist = dist + 1
    return dist

line = input()
steps = line.split(",")
pos = {'x': 0, 'y': 0}
max_dist = 0
for i in steps:
    if i == "ne":
        pos['x'] = pos['x'] + 1
        pos['y'] = pos['y'] + 1
    if i == "se":
        pos['x'] = pos['x'] + 1
        pos['y'] = pos['y'] - 1
    if i == "s":
        pos['y'] = pos['y'] - 2
    if i == "sw":
        pos['x'] = pos['x'] - 1
        pos['y'] = pos['y'] - 1
    if i == "nw":
        pos['x'] = pos['x'] - 1
        pos['y'] = pos['y'] + 1
    if i == "n":
        pos['y'] = pos['y'] + 2
    dist = distance(copy.deepcopy(pos))
    if dist > max_dist:
        max_dist = dist
print(max_dist)