step = 343 #Input
i = 1
k = 0
curr = 0
while i <= 50000000:
    new = (curr + step) % i
    if new == 0:
        k = i
    curr = new + 1
    i = i + 1
print(k)