# greatest among 4 numbers

a = int(input("Enter a number (first) = "))
b = int(input("Enter a number (second) = "))
c = int(input("Enter a number (third) = "))
d = int(input("Enter a number (fourth) = "))

if (a > b and c and d):
    print(f"{a} is the greatest among all")
elif (b > a and c and d):
    print(f"{b} is the greatest among all")
elif (c > b and a and d):
    print(f"{a} is the greatest among all")
else:
    print(f"{d} is the greatest among all")