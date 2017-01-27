fib = [1,2]
total = 0
while (fib[-1] + fib[-2]) <= 4000000:
    fib.append((fib[-1] + fib[-2]))

for i in fib:
    if i % 2 == 0:
        total += i
print(total)
