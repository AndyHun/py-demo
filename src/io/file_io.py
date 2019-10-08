import os
import time
from pathlib import Path

path = '..{}..{}target{}poem.txt'.format(os.sep, os.sep, os.sep)
print('path:', path)

poem = '''{}
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

file = Path(path)

if os.path.exists(path):
    print('{} is already exists! Going to delete it...'.format(path))
    if file.is_file():
        os.remove(path)
    elif file.is_dir():
        os.removedirs(path)

poemFile = open(path, 'w')
poemFile.write(poem)
poemFile.close()

print('Going to open the poem...', end='\r\n\r\n')
rPoem = open(path)
while True:
    line = rPoem.readline()
    if len(line) == 0:
        break
    print(line, end='')
rPoem.close()
