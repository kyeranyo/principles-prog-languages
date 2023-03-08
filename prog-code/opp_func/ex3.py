# Use high-order function approach to write function lstSquare(n:Int) to
# return a list of i square for i from 1 to n?

def lstSquare(x):
    return list(map(lambda a : a**2, [i for i in range(1, x+1)]))

print(lstSquare(3))
print(lstSquare(1))
print(lstSquare(5))
print(lstSquare(4))