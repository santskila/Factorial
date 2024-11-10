print('This program will calculate the factorial of any number')

number = int(input("Type your number here: "))


factorial = 1

for i in range(number + 1):
    if i == 0:
        continue
    factorial = factorial*i

print(f'Your factorial is: {factorial}')
