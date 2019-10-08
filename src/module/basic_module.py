# 1. import python inner module
import sys
# 2. user from...import
from math import sqrt

print('The command line arguments are:')
for arg in sys.argv:
    print(arg)
print('The PYTHONPATH is', sys.path)
print("Square root of 16 is", sqrt(16))

print(__name__)


def basic_hello():
    print("You are calling basic_hello")

__version__ = 0.1
