# 1. How to define a function
def say_hello():
    print('hello world')


# 2. Function local variable
age = 1


def fun_local_variable(age):
    print('local age is', age)
    age = 2
    print('Local age changed to', age)


fun_local_variable(age)
print('global age is still', age)


# 3. Function and global variable
level = 1


def fun_global_variable():
    global level
    print('Using global level within function ', level)
    level = 2
    print('Change global level to ', level)


print('Global level changed to ', level)

# 4. Function and parameter with default value


def fun_default_p(name, healthy=True):
    print('name is', name)
    print('healthy is', healthy)


# 5. Call function via keyword arguments
fun_default_p(healthy=False, name='andy')

# 6.可变参数


def fun_variant_p(a=5, *numbers, **phonebook):
    print('a',a)
    for item in numbers:
        print('item of number is ', item)

    for key, value in phonebook.items():
        print(key, value)


fun_variant_p(10, 1,2,3, jack=123, john=456, tim=789)
# 7, Function with pass


def fun_pass():
    pass


# 8. Function with docstring


def fun_doc_string():
    """这是docstring 开始

    这是docstring 结束"""
    print('running fun_doc_string')


fun_doc_string()
print(fun_doc_string.__doc__)
help(fun_doc_string)