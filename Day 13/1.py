from sys import stdin

firewall = {}
for line in stdin:
    inp = list(map(int, line.split(":")))
    firewall[inp[0]] = inp[1]
sev = 0
for x in firewall:
    if (x) % (firewall[x]-1) == 0 and ((x)/(firewall[x]-1)) % 2 == 0: #Will get caught if time to get there = 2n*(y-1)
        sev = sev + x*firewall[x]
print(sev)