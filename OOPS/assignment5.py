#
# Mohan
#
# pickle and with
#we can also use YAML, JSON instead of pickle
# saving a instance of a class to pickle and retrieve instance from pickle file. execution happens in assignmenttest5.py

import os
import pickle


class MyErrror(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = ''

    def __str__(self):
        if self.message:
            return 'File is not Found error {0} '.format(self.message)
        else:
            return "No error Value Found"


class ConfigDict(dict):

    __CONFIG_DIR = 'conf/'#'/root/PycharmProjects/OOPS/conf/'
    _filename = ''
    __APPENDFLAG = 'wb'

    def __init__(self, filename):

        ConfigDict._filename = os.path.join(ConfigDict.__CONFIG_DIR, filename + '.pickle')
        if not os.path.isfile(self._filename):
            with open(self._filename, self.__APPENDFLAG) as pick:
                pickle.dump({}, pick)
        with open(self._filename, 'rb') as pick:
            pkl = pickle.load(pick)
            self.update(pkl)

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        with open(self._filename, ConfigDict.__APPENDFLAG) as pick:
            pickle.dump(self, pick)

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            print("Given key : {0} is not in Dict available Keys {1}:".format(key, ','.join(self.keys())))


#cd = ConfigDict('config.txt')

#cd['key1'] = 1
#cd['key2'] = 2

#print(cd.keys())