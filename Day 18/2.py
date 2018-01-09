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

def execute(code, regs, i, send_buff, recv_buff):
    command = code[i].split()
    if command[0] == "snd":
        send_buff.append(getValue(command[1], regs))
        return i, 2
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
        if len(recv_buff) != 0:
            regs[command[1]] = recv_buff[0]
            del recv_buff[0]
        else:
            return i, 0
    if command[0] == "jgz":
        if getValue(command[1], regs) > 0:
            i = i + getValue(command[2], regs) - 1
    return i, 1
code = []
regs_0 = {'p':0}
regs_1 = {'p':1}
recv_buff_0 = []
recv_buff_1 = []
for line in stdin:
    code.append(line.strip())
i_0=0
i_1=0
d=0
count = 0
while i_0 < len(code) and i_1 < len(code):
    i_0, d_0 = execute(code, regs_0, i_0, recv_buff_1, recv_buff_0)
    i_1, d_1 = execute(code, regs_1, i_1, recv_buff_0, recv_buff_1)
    if d_0 != 0:
        i_0 = i_0 + 1
    if d_1 != 0:
        i_1 = i_1 + 1
        if d_1 == 2:
            count = count + 1
    if d_0 == 0 and d_1 == 0:
        break
print(count)