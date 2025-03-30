import numpy as np

x = np.random.randint(1,100,size=10)
print(x)

def maior(x):
    return np.max(x)
print(maior(x))