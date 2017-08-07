import random
class Patient(object):
    def __init__(self, name, allergies, bednumber = 0):
        self.id = random.randint(1, 9999999999)
        self.name = name
        self.allergies = allergies
        self.bednumber = bednumber
        self.info = [self.id,self.name,self.allergies,self.bednumber]
    def display_info(self):
        print self.info


class Hospital(object):
    def __init__(self):
        self.patients = []
        self.name = 'Johnnny Hopkins'
        self.capacity = 300
    def add(self,info):
        if len(self.patients)<300:
            self.patients.append(info.info)
            # print self.patients
            for i in self.patients:
                if i[3] == 0:
                    i[3]=len(self.patients)
                    # print i[3]
            # print self.patients
        elif len(self.patients)>=300:
            print 'the hospital is full'
        print self.patients
        return self
    def discharge(self, number):
        discharge = self.patients.pop(number-1)
        for j in range(0,len(discharge)):
            if j == 3:
                discharge[j] = 0
        print discharge
        print self.patients


joe = Patient('Joe Dirt','Feet')
bob = Patient('Finger Licker','Fingers')
sally = Patient('Sally Joe','Bees')
# joe.display_info()

hospital = Hospital()
hospital.add(joe).add(bob).add(sally).discharge(2)
