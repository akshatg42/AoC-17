def convert(moves_, programs_):
    for x in moves_:
        x = x.strip()
        if x[0] == 'x':
            slash = x.find('/')
            first = int(x[1:slash])
            second = int(x[slash+1::])
            first = programs_[first]
            second = programs_[second]
            programs_ = programs_.replace(first, "!").replace(second, first).replace("!", second)
        if x[0] == 's':
            size = int(x[1:])
            swap = programs_[len(programs_)-size:] + programs_
            programs_ = swap[:len(swap)-size]
        if x[0] == 'p':
            first = x[1]
            second = x[3]
            programs_ = programs_.replace(first, "!").replace(second, first).replace("!", second)
    return programs_

line = input()
moves = line.split(",")
l = 0
programs = "abcdefghijklmnop"
original = "abcdefghijklmnop"
rep = 0
for moves_total in range(0, 1000000000):
    if programs == original and moves_total != 0:
        rep = moves_total
        break
    programs = convert(moves, programs)

for moves_total in range(0, 1000000000%rep):
    programs = convert(moves, programs)
print(programs)