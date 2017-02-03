primes = []
x = 2
while True:
    factors = []
    for i in range(1,x+1):
        if x % i == 0:
            factors.append(i)
    if factors == [1,x]:
        primes.append(x)
        factors = []
        x += 1
    else:
        factors = []
        x += 1
    if len(primes) == 100001:
        print(primes[10000])
        break
