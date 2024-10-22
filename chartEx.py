import numpy as np
import matplotlib.pyplot as plt 

with open("measure.txt", "r") as settings:
    tmp = settings.read().split("\n")
    # print((tmp))

with open("res.txt", "r") as data:
    data = data.read().split("\n")
    # print((dat))

tmp = np.array(tmp)
dat = np.array(data)
dat = np.delete(data, -1)
tmp = np.array(tmp, dtype=float)
dat = np.array(dat, dtype=int)
V = dat*0.013
time = []
s = dat.size
for i in range(1, s+1):
    time.append(i/13.4)
print(time)
# print(V)
# print(T)
V = np.array(V)
# T = np.array(T)
plt.title('Процесс заряда и разряда конденсатора в RC-цепях')
plt.xlabel('Напряжение, В')
plt.ylabel('Время, с')
plt.text(1.1,12,r'$Время заряда = $')
plt.text(1.1,12,r'$Время разряда = $')
plt.legend(['V(t)'])
plt.grid(which='major')
plt.minorticks_on()
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.plot(time, V, label='U(t)', linestyle='-', color='blue', linewidth=2, ms=3)
plt.show()

