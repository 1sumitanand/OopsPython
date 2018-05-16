from assignment5 import ConfigDict
import pickle

cc = ConfigDict('config.txt')

cc['key1'] = 1
cc['key3'] = 3
cc['key4'] = 4

print(cc.keys())

print('\n')

del cc['key1']

print(cc.keys())
