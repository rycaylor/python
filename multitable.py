arrh = ['x',1,2,3,4,5,6,7,8,9,10,11,12]
arrt = []
count = 1
for i in range(1,len(arrh),1):
    for count in range(1,13,1):
        v = arrh[i]*count
        arrt.append(v)

print arrt
