from sys import stdin

def getValue(x, regs):
    if str.isalpha(x):
        initReg(x, regs)
        return regs[x]
    else:
        return int(x)
def initReg(x, regs):
    if x not in regs:
        regs[x] = 0

def execute(code, regs, freq, i):
    command = code[i].split()
    if command[0] == "snd":
        return i, getValue(command[1], regs), 0
    if command[0] == "set":
        regs[command[1]] = getValue(command[2], regs)
    if command[0] == "add":
        initReg(command[1], regs)
        regs[command[1]] = regs[command[1]] + getValue(command[2], regs)
    if command[0] == "mul":
        initReg(command[1], regs)
        regs[command[1]] = regs[command[1]] * getValue(command[2], regs)
    if command[0] == "mod":
        initReg(command[1], regs)
        regs[command[1]] = regs[command[1]] % getValue(command[2], regs)
    if command[0] == "rcv":
        if getValue(command[1], regs) != 0:
            print(freq)
            return i, freq, -1
    if command[0] == "jgz":
        if getValue(command[1], regs) > 0:
            i = i + getValue(command[2], regs) - 1
    return i, freq, 0
code = []
regs = {}
for line in stdin:
    code.append(line.strip())
freq = 0
i=0
d=0
while i < len(code) and d == 0:
    i, freq, d = execute(code, regs, freq, i)
    i = i + 1