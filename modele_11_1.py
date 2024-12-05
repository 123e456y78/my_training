import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2, 3])
a_multiplication = a * 2
print(f'a = {a}')
print(f'a_multiplication={a_multiplication}')
print(a.size)
b = np.random.randint(1, size=4)
c = np.random.randint(1, 5, size=(2, 5))
print(f'b = {b}')
print(f'c = {c}')
d = np.arange(1, 10).reshape(3, 3)
print(f'd = {d}')
x = np.dot(a, d)
y = np.dot(d, a)
print(f'x = {x}')
print(f'y = {y}')
# matplotlib
ax1 = plt.subplot(2, 3, 1)
ax1.plot(np.random.random(5))
ax2 = plt.subplot(2, 3, 2)
ax2.plot(np.random.random(5))
ax3 = plt.subplot(2, 3, 3)
ax3.plot(np.random.random(5))
plt.suptitle('Графики', fontsize=28, color='g')
ax1.grid()
ax2.grid()
ax3.grid()
plt.show()