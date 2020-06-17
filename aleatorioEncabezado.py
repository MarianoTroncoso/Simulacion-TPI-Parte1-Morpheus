
import random
aleatorio = 0

contA=0
contB=0
contC=0

for x in range(100):
    aleatorio = random.random()
    if (aleatorio<=0.3):
        contA+=1
    elif (aleatorio<=0.6):
        contB+=1
    else:
        contC+=1


print(contA)
print(contB)
print(contC)
