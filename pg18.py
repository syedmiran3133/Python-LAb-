# wapp to prompt a user to read the marks of 5 subjs
#calculate the total marks and percentage of the marks and
# display the message acccording to the range of %

pp = float(input(" marks of PP = "))
ds = float(input(" marks of ds = "))
dbms = float(input(" marks of dbms = "))
os = float(input(" marks of os = "))
deco = float(input(" marks of deco = "))

total = pp + ds + dbms + os + deco
percent = (total/500) * 100

print(f"Total = {total}")
print(f"percentage = {percent}%")

if (percent >= 90):
    print("Distinction")
elif (percent >= 80 and percent < 90):
    print("First class")
elif (percent >= 70 and percent < 80):
    print("Second class")
elif (percent >= 60 and percent < 70):
    print("Pass")
else:
    print("fail")