print('This program will calculate the factorial of any number') #Show what the program does

number = int(input("Type your number here: ")) #Gets the number from the user

factorial = 1

for i in range(number + 1): #Calculates the factorial
    if i == 0:
        continue
    factorial = factorial*i

print(f'Your factorial is: {factorial}') #Show the results
