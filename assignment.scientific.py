# a) Plot a line graph representing the temperature readings over a week
import matplotlib.pyplot as plt

temperatures = [20, 22, 19, 23, 21, 24, 20]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

plt.plot(days, temperatures, marker='o')
plt.title('Temperature Readings Over a Week')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# b) Generate the arithmetic sequence starting at 5 with a common difference of 3, for 8 terms
start = 5
diff = 3
terms = 8
sequence = [start + diff * i for i in range(terms)]
print("Arithmetic sequence:", sequence)

# c) Calculate the volume under the surface z = x^2 + y^2 over the square region 0 ≤ x, y ≤ 1
from scipy.integrate import dblquad

def integrand(y, x):
    return x**2 + y**2

volume, error = dblquad(integrand, 0, 1, lambda x: 0, lambda x: 1)
print("Volume under z = x^2 + y^2 over [0,1]x[0,1]:", volume)

# d) Explanation
explanation = """
Compiled languages translate the entire source code into machine code before execution, resulting in faster runtime performance. Examples include C and C++.
Interpreted languages execute code line by line at runtime, which makes debugging easier but can be slower. Examples include Python and JavaScript.
Python is an interpreted language, as its code is executed by the Python interpreter line by line.
"""
print(explanation)