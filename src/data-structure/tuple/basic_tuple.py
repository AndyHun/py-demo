# 1 how to define a tuple
zooOne = ('python', 'elephant')
print('zooOne looks like', zooOne)
print('Number of zooOne is', len(zooOne))

zooTwo = 'monkey', 'camel', zooOne
print('zooTwo look like', zooTwo)
print('Number of zooTwo is', len(zooTwo))

print(zooTwo[2][0])

# 2 empty tuple
emptyTuple = ()

# 3 contain only one item tuple, do not assign (2), it's an object
sigleItemTuple = (2,)
print(sigleItemTuple)

# 4 check element
if 'python' in zooOne:
    print('Yes, we have python')
