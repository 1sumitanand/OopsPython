class SumList():

    def __init__(self, thislist):
        self.thislist = thislist


    def __add__(self, other):

        new_list = [ x + y for x, y in zip(self.thislist, other.thislist)]

        return SumList(new_list)

    def __repr__(self):
        return str(self.thislist)



cc = SumList([1,2,3,4,5])
dd = SumList([10,20,30,40,50])

ee = cc + dd
print(ee)