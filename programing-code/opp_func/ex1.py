# Use recursive approach to write a function lstSquare(n:Int) that
# returns a list of the squares of the numbers from 1 to n?

# print(lstSquare(3)) -> [1, 4, 9]
def lstSquare(x):
    if x == 1:
        return [1]
    else:
        return lstSquare(x-1) + [x**2]

print(lstSquare(3))
print(lstSquare(1))
print(lstSquare(5))
print(lstSquare(4))