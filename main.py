#Question1
function1 = lambda x: (x - 3) / x ** 2
number1 = int(input("Please enter a number: "))
list = []
calculateTo = number1 +1
for a in range(1, calculateTo, 1):
    list.append(function1(a))
print(sum(list))


#Question2
def recursive(n):
    #This is a function that calculate as ((n / (n + 2)) - 10) * recursive(n - 1)
    if n == 0:
        return 1
    else:
        return ((n / (n + 2)) - 10) * recursive(n - 1)


number2 = int(input("Please neter another number: "))
print(recursive(number2))
