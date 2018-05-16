#
#   Mohan
# sample to show Inheritance polymorphism and Encapsulation
#  Inheriting dict class
#  Polymorphism ConfigDict class reacts differently on Read and write.
#  Encapsulation _filename variable is made private to class can be acc

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

    def __setitem__(self, key, val):
        # below command is same as dict.__setitem__(self, k, v.strip("\n")) but below command is the best way
        super(ConfigDict, self).__setitem__(key, val)

        with open(self._filename, self._append_flag) as self.fbuffer:
         self.fbuffer.write(str(key) + '=' + str(val) + '\n')

        self._append_flag = 'a'


#class ConfigDict(DoThis):
#    pass
    #def __setitem__(self, key, val):

    #    super(ConfigDict, self).__setitem__(key, val)
    #

cd = ConfigDict('config_file.txt')

#cd['key1'] = 100
#cd['key2'] = 2
#cd['key3'] = 3
#cd['key4'] = 4


print(cd.keys())
print(cd)