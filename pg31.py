# Python code to
# find sum of square of
# first n even numbers

def squareSum(n):
    sum = 0
    for i in range(0, n + 1):
        sum += (2 * i) * (2 * i)

    return sum
ans = squareSum(10)
print(ans)
