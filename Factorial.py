def factorial(numF):
    if numF <= 1:
        return 1
    return numF * factorial(numF - 1)

print("Type a number")

num = input()
num = int(num)

print(factorial(num))