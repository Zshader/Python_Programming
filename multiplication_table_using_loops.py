abc = int(input("Please enter a number to know it is prime or not: "))

# i = 1

# while i <= 10:
#     print (abc, " x ", i , "=", abc * i)
#     i = i + 1

#Prime Number

for items in range(2,abc):
    if abc%items == 0:
        print(f"{abc} is not a prime number and is divisible by: {items}")
        break
else:
    print(f"{abc} is a prime number")

