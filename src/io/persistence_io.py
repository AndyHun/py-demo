import os
import pickle
from pathlib import Path

shopList = ['apple', 'carrot']
fPath = '..{}..{}target{}shot_list.data'.format(os.sep, os.sep, os.sep)
fData = Path(fPath)

if os.path.exists(fPath):
    print('shot_list.data already exists! Going to delete it...')
    if fData.is_file():
        os.remove(fPath)
    elif fData.is_dir():
        os.removedirs(fPath)

dataFile = open(fPath, 'wb')
pickle.dump(shopList, dataFile)
dataFile.close()

del shopList
del dataFile

dataFile = open(fPath, 'rb')
storedList = pickle.load(dataFile)
print(storedList)
