# Let lst be a list of a list of element,
# use recursive approach to write function flatten(lst) that returns the list of all elements

# flatten([[1,2,3],[4,5],[6,7]]) -> [1,2,3,4,5,6,7]

def flatten(lst):
    if lst:
        return lst[0] + flatten(lst[1:])
    else:
        return []

print(flatten([[1,2,3],[4,5],[6,7]]))
print(flatten([[]]))
print(flatten([]))
print(flatten([[1,2,3]]))
print(flatten([[1],[2],[3],[4],[5,6,7]]))