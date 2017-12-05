n = int(input())
x = 1
y = 1
while x*x < n:
    x = x+2
y = x-2
y = y*y
while n - y >= x:
    n = n-x+1
quo = (n - y) % (x)
out = int(x/2) + int(abs(quo - int(x/2)))
print(out)