# Let lst be a list of integer and n be any value, use list
# comprehension approach to write function dist(lst,n) that
# returns the list of pairs of an element of lst and n.

def dist(lst, n):
    res = []
    for i in lst:
        res.append((i, n))
    return res


print(dist([1,2,3],4))
print(dist([],4))
print(dist([1,2,3],'a'))
print(dist([3,4,1,5],6))
print(dist([1],'a'))