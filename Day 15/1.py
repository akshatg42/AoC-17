cons_a = 16807
cons_b = 48271
val_a = 873
val_b = 583
macx = 2147483647
count = 0
for i in range(40000000):
    val_a = (val_a * cons_a) % macx
    val_b = (val_b * cons_b) % macx
    if "{:32b}".format(val_a)[16:] == "{:32b}".format(val_b)[16:]:
        count = count + 1
print(count)