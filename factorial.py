
abc = int(input("Lets calculate the Factorial of a number, \n Please enter a number to calculate its factorial: "))

# i=1


def fact(abc):
    fact1 = abc

    for i in range(1, abc):
        fact1 = fact1*(abc-i)

    return fact1

factorial1 = fact(abc)
print(factorial1)