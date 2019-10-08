# 1. how to format a string
age = 20
name = 'Andy'
print('#1: {0} was {1} years old when he wrote this bool'.format(name, age))

# 2. how to assign a string with break line(i.e. multiple line string)
articl = '''
This is a book.
It's owned by {}
'''
print('#2: {}', articl.format(name))

# 3. 对于浮点数 '0.333' 保留小数点(.)后三位
print('#3: {0:.3f}'.format(1.0 / 3))
# 4. 使用下划线填充文本，并保持文字处于中间位置, 使用 (^) 定义 '___hello___'字符串长度为 11
print('#4: {0:_^11}'.format('hello'))
# 5. 基于关键词输出 'Swaroop wrote A Byte of Python'
print('#5: {name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# 6. 替换print换行符
print('#6: a', end=';')
print('b', end=';')
print('c', end=';')

# 7. Non Raw String
print('#7: Tab is enable here \t.')

# 8. Raw String
print(r'#8: Tab is indicated by \t.')

# 9. startswith
print('#9', name.startswith('A'))

# 10. find
print('#10', name.find('n'))
