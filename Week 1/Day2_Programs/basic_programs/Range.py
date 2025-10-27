terms = int(input("Enter a number: "))
sum = 0
for i in range(1, terms + 1):
    sum+= i * i
print(f"Sum of squares of first {terms} natural numbers is: {sum}")
