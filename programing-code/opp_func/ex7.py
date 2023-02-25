# Let lst be a list of integer and n be an integer, use recursive approach
# to write function lessThan(lst,n) that returns the list of
# all numbers in lst less than n.

# lessThan([1,2,3,4,5],4) -> [1,2,3]
def lessThan(lst, n):
    if lst:
        if lst[0] < n:
            return [lst[0]] + lessThan(lst[1:], n)
        else:
            return [] + lessThan(lst[1:], n)
    else:
        return []

print(lessThan([1,2,3,4,5],4))
print(lessThan([],4))
print(lessThan([5,2,6,4,1],4))
print(lessThan([7,6,4,4,5],4))
print(lessThan([1,2,3,-1,0],4))