# 1 define a list
shoplist = ['apple', 'mango', 'carrot']
print('I have', len(shoplist), 'itmes to purchase');
print('These items are:', end=' ')
for item in shoplist:
    print(item, end=',')

# 2 append
shoplist.append('rice')
print('\nAfter append. Now, my shopping list are', shoplist)

# 3 sort
shoplist.sort()
print('After sort. Now, my shopping list are', shoplist)

# 4 how to get
oldItem = shoplist[0]
del shoplist[0]
print('After bought one, now, my shopping list are', shoplist)

# 5 check element
if 'rice' in shoplist:
    print('Yes, we need to shop rice')

# 6 slice list
idList = [0, 1, 2, 3, 4, 5, 6]
print('idList[0:1]', idList[0:1])
print('idList[:1]', idList[:1])
print('idList[:]', idList[:])
print('idList[0:]', idList[0:])
print('idList[:-1]', idList[0:-1])
print('idList[-2:-1]', idList[-2:-1])
# 7 slice list with step 2
print('idList[::2]', idList[::2])

# 8 join separator
print('#8', ";".join(shoplist))
