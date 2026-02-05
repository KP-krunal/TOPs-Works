# Write a Prgram to find the factorial of given number

num = int(input("Enter a number to find factorial: "))
ans = 1
for i in range(1, num + 1):
    ans = ans * i
print("Factorial of", num, "is:", ans)
