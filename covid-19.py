import math
import matplotlib.pyplot as plt
total = []
hari = []
class Orang:
    def __init__(self,R,P):
        self.R = R
        self.P = P
Nh = 100
newOrang = Orang(50,0.01)
temp = newOrang.R * newOrang.P
Nh = (1 + temp)
for i in range(0,15):
    NhNew = (math.pow(Nh,i)) * 100
    total.append(NhNew)
    hari.append(i)

plt.figure()
plt.plot(hari, total, 'r')
plt.title('prediksi berakhir covid-19 dengan matematika')
plt.show()