import random
class Call(object):
    def __init__(self,name,time,reason):
        self.id = random.randint(1000000000, 9999999999)
        self.caller_name = name
        self.time = time
        self.reason = reason
        self.info = [self.caller_name,self.id,self.time,self.reason]
    def display_info(self):
        print self.info

class Call_center(object):
    def __init__(self):
        self.calls = []
        self.qeue = len(self.calls)
    def add(self,info):
        print info.info
        self.calls.append(info.info)
        print self.calls
        self.qeue = len(self.calls)
        print self.qeue
        return self
    def remove(self):
        self.calls.pop(0)
        self.qeue = len(self.calls)
    def callinfo(self):
        for i in self.calls:
            print i[0]
            print i[1]


acall = Call('Joe','1:00','Back-scratcher')

center =Call_center()
center.add(acall).callinfo()
# acall.display_info()
