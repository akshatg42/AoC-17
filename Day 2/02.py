from sys import stdin
sum=0
for line in stdin:
    b = False
    numbers = list(map(int, line.split()))
    for x in numbers:
        b = False
        for y in numbers:
            if x == y:
                continue
            if x%y == 0:
                sum = sum + x/y
                b = True
                break
        if b:
            break
print(sum)