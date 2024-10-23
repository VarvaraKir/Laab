import numpy as np
import matplotlib.pyplot as plt

with open("measure.txt", "r") as settings:
    tmp = settings.read().split("\n")
    # print((tmp))

with open("res.txt", "r") as data:
    data = data.read().split("\n")
    # print((dat))

tmp = np.array(tmp, dtype=float)
dat = np.array(data, dtype=int)

V = dat * 0.013
step = 0.011
n = len(dat)
time = np.linspace(0, step * n, n)
print(time)


V = np.array(V)

plt.plot(time, V, label="U(t)", linestyle="-", marker ="o", color="blue", linewidth=2, markersize=4,
         markevery=20)
plt.title("Процесс заряда и разряда конденсатора в RC-цепях")
plt.ylabel("Напряжение, В")
plt.xlabel("Время, с")
plt.text(6,2,f"Время зарядки: 4.24 c \nВрямя разрядки: 5.66 c")
plt.grid(which="major")
plt.minorticks_on()
plt.grid(which="minor", linestyle=":")
plt.tight_layout()
plt.legend()
plt.show()
print('\a')
