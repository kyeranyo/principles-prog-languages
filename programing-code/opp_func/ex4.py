# Let lst be a list of integer and n be any value, use recursive approach to write function dist(lst,n) that
# returns the list of pairs of an element of lst and n.

# dist([1,2,3],4) -> [(1, 4),(2, 4),(3, 4)]
def dist(lst, n):
    if lst:
        return [(lst[0], n)] + dist(lst[1:], n)
    else:
        return []

print(dist([1,2,3],4))
print(dist([],4))
print(dist([1,2,3],'a'))
print(dist([3,4,1,5],6))
print(dist([1],'a'))