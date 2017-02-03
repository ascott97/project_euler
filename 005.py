
def div_1_20(number):
    div_count = 0
    for i in range(1,21):
        if number % i == 0:
            div_count += 1
        else:
            return False
    if div_count == 20:
        return True

x = 20          #Has to be divisible by 20, less num checks if +20 each time
while not div_1_20(x):
    x += 20

print(x)
