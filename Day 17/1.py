array = [0]
step = 343 #Input
i = 1
curr = 0
while i <= 2017:
    new = curr + step
    new = new % len(array)
    array.insert(new+1, i)
    curr = new+1
    i = i + 1
print(array[(curr+1)%len(array)])