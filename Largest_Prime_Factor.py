def factors(num):
    factors = []
    x = 2
    while True:
        if num % x == 0:
            factors.append(x)
            print(factors)
            num /= x
            x += 1
        else:
            x += 1




factors(600851475143)
