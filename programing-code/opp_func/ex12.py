# Let lst be a list of a list of element, use high-order function approach
# to write function flatten(lst) that returns the list of all elements

from functools import reduce
def flatten(lst):
    if not lst :
        return []
    return list(reduce(lambda a, b: a + b, lst))

print(flatten([[1,2,3],[4,5],[6,7]]))
print(flatten([[]]))
print(flatten([]))
print(flatten([[1,2,3]]))
print(flatten([[1],[2],[3],[4],[5,6,7]]))