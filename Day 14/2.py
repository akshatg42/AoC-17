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

def count_regions(disk):
    count = 0
    for x in range(128):
        for y in range(128):
            if disk[x][y] == 1:
                count = count + 1
                dfs(disk, x, y, count)
    return count

def dfs(disk, x, y, count):
    disk[x][y] = -1 * count
    if x+1 < 128 and disk[x+1][y] == 1:
        dfs(disk, x+1, y, count)
    if y+1 < 128 and disk[x][y+1] == 1:
        dfs(disk, x, y+1, count)
    if y-1 < 128 and y-1 >= 0 and disk[x][y-1] == 1:
        dfs(disk, x, y-1, count)
    if x-1 < 128 and x-1 >= 0 and disk[x-1][y] == 1:
        dfs(disk, x-1, y, count)

inp = """uugsqrei"""
disk = []
lengths = []
for l in range(128):
    lengths = []
    inp_ = inp + '-' + str(l)
    for x in inp_:
        lengths.append(ord(x))
    lengths = lengths + [17, 31, 73, 47, 23]
    dense_hash = knot_hash(lengths)
    row = []
    row_ = []
    for z in dense_hash:
        row.append("{:08b}".format(z))
    for x in row:
        r = list(x)
        for y in r:
            row_.append(int(y))
    disk.append(row_)
print(count_regions(disk))