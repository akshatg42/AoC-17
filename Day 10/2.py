line = """189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62"""
lengths = []
for x in line:
    lengths.append(ord(x))
lengths = lengths + [17, 31, 73, 47, 23]
array = []
for x in range(0, 256):
    array.append(x)
curr = 0
skip_size = 0
for z in range(64):
    for x in lengths:
        new_array = []
        for y in range(curr, curr+x):
            new_array.append(array[y%len(array)])
        for y in range(curr, curr+x):
            array[y%len(array)] = new_array[len(new_array) - 1 - y + curr]
        curr = curr + x + skip_size
        curr = curr % len(array)
        skip_size = skip_size + 1
dense_hash = []
for z in range(16):
    val = 0
    for x in range(16*z, 16*(z+1)):
        val = val ^ array[x]
    dense_hash.append(val)
ans = ""
for z in dense_hash:
    ans = ans + "{:02x}".format(z)
print(ans)