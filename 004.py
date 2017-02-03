def is_palindrome(number):
    matches = len(str(number)) // 2
    first_half = []
    last_half = []
    for i in range(0, matches):
        first_half.append(str(number)[i])
    for j in range(1, (matches + 1)):
        last_half.append(str(number)[-j])
    if first_half == last_half:
        return True

palindromes = []
x = 999
while x > 0:
    for i in range(1, x+1):
        product = x * i
        if is_palindrome(product):
            palindromes.append(product)
    x -= 1

print(sorted(palindromes))
