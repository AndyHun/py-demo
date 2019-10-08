# 1 how to init a set
bookSet = set(['B1', 'B2', 'B3'])
bookSet_same = set(['B1', 'B2', 'B3'])
print('We have book B1', 'B1' in bookSet)

# 2. copy
bookSet2 = bookSet.copy()
print('bookSet == bookSet2', bookSet == bookSet2)
print('bookSet is bookSet2', bookSet is bookSet2)
bookSet2.remove('B1')
print('After remove B1 from bookSet2, bookSet == bookSet2', bookSet == bookSet2)
print('bookSet == bookSet_same', bookSet == bookSet_same)
bookSet2.add('B4')
print('bookSet == bookSet2', bookSet == bookSet2)

# 3. is superset
bookSet2.issubset(bookSet)

# 4 intersection
print('bookSet & bookSet2', bookSet & bookSet2)
print('bookSet.intersection(bookSet2)', bookSet.intersection(bookSet2))
