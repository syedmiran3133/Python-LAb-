# python program to find sum of digits of given number


def getSum(n):
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)


n = 12345
print(getSum(n))