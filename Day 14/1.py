def knot_hash(lengths):
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
    return dense_hash

inp = """uugsqrei"""
disk = 0
lengths = []
for l in range(128):
    lengths = []
    inp_ = inp + '-' + str(l)
    for x in inp_:
        lengths.append(ord(x))
    lengths = lengths + [17, 31, 73, 47, 23]
    dense_hash = knot_hash(lengths)
    ans = 0
    for z in dense_hash:
        ans = ans + bin(z).count("1")
    disk = disk + ans
print(disk)