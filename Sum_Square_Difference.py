a = 0
b = 0

for i in range(1,101):
    a += i**2
for j in range(1,101):
    b += j

b = b**2

print(b-a)
