def factorial(numF):
    if numF <= 1:
        return 1
    return numF * factorial(numF - 1)

print("Type a number")

num = input()
num = int(num)

print(factorial(num))


# Adding an itertive version since you can cry about it

def factorialIterative(num):
    ans = num
    while num > 0:
        num -= 1
        ans *= num
    return ans

print(factorialIterative(num))
