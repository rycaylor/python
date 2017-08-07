class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def ride(self):
        self.miles += 10
        return self
    def reverse(self):
        self.miles -= 5
        return self
    def displayinfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self


bike1 = Bike("$1,0000,000","15 MPH")
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()

bike2 = Bike("$200", "60 MPH")
bike2.ride().ride().ride().ride()
bike2.displayinfo()
bike3 = Bike("$1,500", "35 MPH")
bike3.ride().ride().ride().ride().ride().ride().ride().ride()
bike3.reverse().reverse().reverse()
bike3.displayinfo()

print bike1
print bike2
print bike3
