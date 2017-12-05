from sys import stdin
valid=0
for line in stdin:
    words = line.split()
    if len(words) == len(set(words)):
        valid=valid+1
print(valid)