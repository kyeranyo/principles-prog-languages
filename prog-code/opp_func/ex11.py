# Let lst be a list of a list of element, use list comprehension
# approach to write function flatten(lst) that returns the list of all elements

def flatten(lst):
    res = []
    for i in lst :
        res += i
    return res

print(flatten([[1,2,3],[4,5],[6,7]]))
print(flatten([[]]))
print(flatten([]))
print(flatten([[1,2,3]]))
print(flatten([[1],[2],[3],[4],[5,6,7]]))