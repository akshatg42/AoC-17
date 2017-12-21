from sys import stdin

firewall = {}
for line in stdin:
    inp = list(map(int, line.split(":")))
    firewall[inp[0]] = inp[1]
wait = 0

while True:
    f = True
    for x in firewall:
        if (wait + x) % (firewall[x]-1) == 0 and ((wait + x)/(firewall[x]-1)) % 2 == 0: #Will get caught if time to get there = 2n*(y-1)
            f = False
            break
        else:
            f = f and True
    if not f:
        wait = wait + 1
    else:
        print(wait)
        break