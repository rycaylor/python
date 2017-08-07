class MathDojo(object):
    def __init__(self, initial):
        self.initial = initial
        print initial
    def add(self, x, y = 0):
        if isinstance(y,list) and isinstance(x,list):
            r = 0
            for p in range(0,len(y)):
                r += y[p]
            b = 0
            for t in range(0,len(x)):
                b += x[t]
            add = b + r + self.initial
        elif isinstance(y,list):
            r = 0
            for p in range(0,len(y)):
                r += y[p]
            add = x + r + self.initial
        elif isinstance(x,list):
            b = 0
            for t in range(0,len(x)):
                b += x[t]
            add = y + b + self.initial
        else:
            add = x + y + self.initial
        print add
        return self
    def subtract(self, z, j = 0):
        if isinstance(j,list) and isinstance(z,list):
            r = 0
            for p in range(0,len(j)):
                r += j[p]
            b = 0
            for t in range(0,len(z)):
                b += z[t]
            sub = self.initial - r - b
        elif isinstance(j,list):
            r = 0
            for p in range(0,len(j)):
                r += j[p]
            sub = self.initial - r - z
        elif isinstance(z,list):
            b = 0
            for t in range(0,len(z)):
                b += z[t]
            sub = self.initial - b - j
        else:
            sub = self.initial - z - j
        print sub
        return self

md = MathDojo(2)
md.add(12,25).subtract([1000,13000,10],1)
