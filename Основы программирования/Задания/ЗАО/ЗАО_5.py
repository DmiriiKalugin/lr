import math

a = math.radians(360) 
b = 16 * (math.cos(a/17))
print(a)
c = math.sqrt(34 - 2 * math.sqrt(17)) + math.sqrt(17) - 1 + 2 * math.sqrt(17) + 3 * math.sqrt(17) \
    - math.sqrt(170 + 38 * math.sqrt(17))
print(c)
print(b == c)
input()
