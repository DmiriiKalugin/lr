import random

x = list((10, 5, 20, 1))
mi = min(x)
ma = max(x)
print(x)
for i in range(len(x)):
    if x[i] == mi:
        x[i] = ma
    elif x[i] == ma:
        x[i] = mi
print(x)



