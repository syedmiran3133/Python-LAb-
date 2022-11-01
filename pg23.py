# adding consecutive numbers using while loop


a = int(input("enter number upto = "))
num = 1
sum = 0
while num<=a:
   sum += num
   num += 1

print(f"Sum of numbers from 1 to {a} is {sum}")