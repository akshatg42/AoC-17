line = input()
moves = line.split(",")
programs = "abcdefghijklmnop"
for x in moves:
    x = x.strip()
    if x[0] == 'x':
        slash = x.find('/')
        first = int(x[1:slash])
        second = int(x[slash+1::])
        first = programs[first]
        second = programs[second]
        programs = programs.replace(first, "!").replace(second, first).replace("!", second)
    if x[0] == 's':
        size = int(x[1:])
        swap = programs[len(programs)-size:] + programs
        programs = swap[:len(swap)-size]
    if x[0] == 'p':
        first = x[1]
        second = x[3]
        programs = programs.replace(first, "!").replace(second, first).replace("!", second)
print(programs)