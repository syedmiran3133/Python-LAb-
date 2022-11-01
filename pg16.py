# WAPP to test wheather a number is divisible by 5 & 10 or 5 or 10?

a = int(input("Enter a number = "))

if ((a % 5 == 0) and (a % 10 == 0)):
    print(f"The number {a} is divisible by 5 and 10")
elif ((a % 5 == 0) or (a % 10 == 0)):
    print(f"The number {a} is divisible by 5 or 10")
else:
    print("not divisible")