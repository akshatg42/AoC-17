from sys import stdin

Left = set()
Right = set()
for line in stdin:
    line = line.strip()
    left = line.split("(")[0]
    right = line.split(")")[1].split("->")
    Left.add(left.strip())
    for x in right:
        x = x.split(",")
        for i in x:
            i = i.strip()
            if len(i) > 0:
                Right.add(i)
print(Left - Right)
