from sys import stdin
sum=0
for line in stdin:
    b = False
    numbers = list(map(int, line.split()))
    sum = sum + max(numbers) - min(numbers)
print(sum)