line = input()
lengths = list(map(int, line.split(",")))
array = []
for x in range(0, 256):
    array.append(x)
curr = 0
skip_size = 0
for x in lengths:
    new_array = []
    for y in range(curr, curr+x):
        new_array.append(array[y%len(array)])
    for y in range(curr, curr+x):
        array[y%len(array)] = new_array[len(new_array) - 1 - y + curr]
    curr = curr + x + skip_size
    curr = curr % len(array)
    skip_size = skip_size + 1
print(array[0]*array[1])