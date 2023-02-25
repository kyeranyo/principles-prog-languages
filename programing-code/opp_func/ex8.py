# Let lst be a list of integer and n be an integer, use list comprehension approach
# to write function lessThan(lst,n) that returns the list of all numbers in lst less than n.

def lessThan(lst, n):
    res = []
    for i in lst:
        if i < n:
            res.append(i)
    return res

print(lessThan([1,2,3,4,5],4))
print(lessThan([],4))
print(lessThan([5,2,6,4,1],4))
print(lessThan([7,6,4,4,5],4))
print(lessThan([1,2,3,-1,0],4))