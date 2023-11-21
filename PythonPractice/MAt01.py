import matplotlib.pyplot as plt
import numpy as np


def function():
    experience = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    salaries = np.array([15, 20, 23, 29, 30, 28, 35, 45, 48, 50])

    plt.scatter(experience, salaries, color='black', label='Salary')
    plt.plot(experience, salaries, color='blue', label='experience')
    plt.xlabel("Experience (in year)")
    plt.ylabel("salary(in k)")
    plt.title(" Experience vs salaries")
    plt.legend()
    plt.savefig("experience vs salary graph.jpg")
    plt.show()



function()
