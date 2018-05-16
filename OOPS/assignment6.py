#
# Mohan
#
# testing class for pytest module to test, test case found in assignmenttest6

import os


class MyError(Exception):

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

    def __init__(self, filename):
        self._filename = filename
        self._append_flag = 'w'
        if os.path.isfile(self._filename):
            with open(self._filename, 'r') as self.rbuffer:
                self.lines = self.rbuffer.readlines()
            for val in self.lines:
                k, v = val.split('=', 1)
                # below command is same as super(ConfigDict, self).__setitem__(key, val)
                dict.__setitem__(self, k, v.strip("\n"))
        else:
            raise MyError("File Dosen\'t  Exist")

    def __setitem__(self, key, val):
        # below command is same as dict.__setitem__(self, k, v.strip("\n")) but below command is the best way
        super(ConfigDict, self).__setitem__(key, val)

        with open(self._filename, self._append_flag) as self.fbuffer:
         self.fbuffer.write(str(key) + '=' + str(val) + '\n')

        self._append_flag = 'a'


    def __getitem__(self, key):
        if key not in self.keys():
            raise KeyError
        else:
            return dict.__getitem__(self, key)



