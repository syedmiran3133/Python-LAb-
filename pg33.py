# python program to find sum of numbers from 1 to 30 which are divisible by 3 and 5

lower = int(input("Enter lower range limit:"))
upper = int(input("Enter upper range limit:"))
for i in range(lower, upper+1):
   if((i%3==0) & (i%5==0)):
      print(i)
