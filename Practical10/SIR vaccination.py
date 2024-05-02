import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000
beta = 0.3
gamma = 0.05

vaccination_rates = np.arange(0, 1.1, 0.1)
I_arrs = []

for vaccination_rate in vaccination_rates:
    V = vaccination_rate * N
    S = N - V
    I = 1
    R = 0

    S_arr = [S]
    I_arr = [I]
    R_arr = [R]

    for t in range(1000):
        if S == 0:
            break

        contact_rate = beta * (I / (N - V))
        new_infections = np.random.choice([0, 1], size=int(S), p=[1 - contact_rate, contact_rate])
        new_recoveries = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma])

        I += np.sum(new_infections) - np.sum(new_recoveries)
        S -= np.sum(new_infections)
        R += np.sum(new_recoveries)

        S = max(S, 0)
        I = max(I, 0)
        R = max(R, 0)

        S_arr.append(S)
        I_arr.append(I)
        R_arr.append(R)

    I_arrs.append(I_arr)

for i, I_arr in enumerate(I_arrs):
    plt.plot(I_arr, label=f'{vaccination_rates[i] * 100:.1f}% Vaccinated', color=cm.viridis(i / len(vaccination_rates)))

plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend()
plt.show()