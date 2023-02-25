# Use list comprehension approach to write a function lstSquare(n:Int) that
# returns a list of the squares of the numbers from 1 to n?

def lstSquare(x):
    res = []
    for i in range(1, 1+x):
        res.append(i**2)
    return res

print(lstSquare(3))
print(lstSquare(1))
print(lstSquare(5))
print(lstSquare(4))