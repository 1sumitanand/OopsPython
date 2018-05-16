#
#
#   Mohan
# using "with" command to handle file open and close after the reads or write automatically without using file.close()
#


import os
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
            raise MyErrror("File Dosen\'t  Exist")

    def __setitem__(self, key, val):
        # below command is same as dict.__setitem__(self, k, v.strip("\n")) but below command is the best way
        super(ConfigDict, self).__setitem__(key, val)

        with open(self._filename, self._append_flag) as self.fbuffer:
         self.fbuffer.write(str(key) + '=' + str(val) + '\n')

        self._append_flag = 'a'


    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            print("Given key : {0} is not in Dict available Keys {1}:".format(key, ','.join(self.keys())))



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


cd = ConfigDict('config_file.txt')

#cd['key1'] = 100
#cd['key2'] = 2
#cd['key3'] = 3
#cd['key4'] = 4


print(cd['key'])