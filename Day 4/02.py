from sys import stdin

def anagramCheck(str1, str2):
    return sorted(str1) == sorted(str2)

valid=0
for line in stdin:
    words = line.split()
    if len(words) == len(set(words)):
        b=True
        for x in words:
            for y in words:
                if x!=y and anagramCheck(x, y):
                    b=False
                    break
        if b:
            valid=valid+1
print(valid)