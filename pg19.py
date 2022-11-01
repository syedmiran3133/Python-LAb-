# WAPP to prompt a user to enter a day of the week
# If entered day of the week is between 1 and 7 then display
# respective name of the day

day = int(input("Enter the number 1 - 7 = "))

if (day==1):
    print(f"{day} is Sunday")
elif (day==2):
    print(f"{day} is Monday")
elif (day==3):
    print(f"{day} is Tuesday")
elif (day==4):
    print(f"{day} is Wednesday")
elif (day==5):
    print(f"{day} is Thursday")
elif (day==6):
    print(f"{day} is Friday")
elif (day==7):
    print(f"{day} is Saturday")
else:
    print("Wrong input")