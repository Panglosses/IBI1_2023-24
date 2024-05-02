import numpy as np
import matplotlib . pyplot as plt
N = 10000  
S = N - 1  
I = 1      
R = 0      

beta = 0.3  
gamma = 0.05  

S_arr = [S]
I_arr = [I]
R_arr = [R]

# for each time step from 1 to 1000:
#     1. Calculate the number of new infections and new recoveries
#     2. Update the number of susceptible, infected, and recovered individuals
#     3. Record the output for each time step
for t in range(1000):
    # Calculate the number of new infections and recoveries
    # The probability of a susceptible individual becoming infected is beta * (I/N)
    # The probability of an infected individual recovering is gamma
    new_infections = np.random.choice([0, 1], size=S, p=[1 - beta * (I/N), beta * (I/N)])
    new_recoveries = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma])

    I += np.sum(new_infections) - np.sum(new_recoveries)
    S -= np.sum(new_infections)
    R += np.sum(new_recoveries)

    S = max(0, S)
    I = max(0, I)
    R = max(0, R)

    S_arr.append(S)
    I_arr.append(I)
    R_arr.append(R)

plt.plot(S_arr, label='Susceptible')
plt.plot(I_arr, label='Infected')
plt.plot(R_arr, label='Recovered')

plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model Simulation')

plt.legend()

plt.show()