#!python3

import matplotlib.pyplot as plt

def attack_fomula(n):
    return lambda a,b:n*((a/100)+1)*((b/100)+1)
    
def reg(x,y):
    coefficients = np.polyfit(x,y,1) 
    p = np.poly1d(coefficients) 
    return coefficients, p
    
ultima = attack_fomula(2100)
args = [142,964]
print(ultima(*args))
L = []
for i in range(13):
    L.append([138+i*5,918+(12-i)*8])
    #print(ultima(*L[i]))
#print(L)
(arg1, arg2), fomula = reg(**L)

   