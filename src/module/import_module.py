# 1 import module from same path
import basic_module


# 2 import module from nested folder
# 2.1method 1
# import chmodule.ch_hello as ch_hello
# 2.2method 2
from chmodule import ch_hello
import sys

ch_hello.hello()

# should print origin module name - basic_module
print(__name__)
print(basic_module.__name__)

# 3 import module from absolute path
# 3.1 use sys
sys.path.append('..')  # 添加上层path
sys.path.append(r"C:\WorkSpace\GTC\py-demo\src\module")  # 添加绝对path


# 4 use path
# python will scan $python\Lib\site-packages下的.pth文件, 可将路径写入该文件即可
