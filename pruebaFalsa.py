import random

def GeneraTiempo2():
    aleatorio=0
    respuesta = 0
    aleatorio = random.random()
    if(aleatorio <=0.015):
        respuesta = 1
    elif(aleatorio<=0.1):
        respuesta = 2
    elif(aleatorio<=0.25):
        respuesta = 3
    elif(aleatorio<=0.30):
        respuesta = 4
    elif(aleatorio<=0.60):
        respuesta = 5
    else: 
        respuesta = 6
    return respuesta

def GeneraSiguiente2():
    aleatorio=0
    respuesta = 0
    aleatorio = random.random()
    if(aleatorio <=0.015):
        respuesta = 4
    elif(aleatorio<=0.1):
        respuesta = 6
    elif(aleatorio<=0.25):
        respuesta = 7
    elif(aleatorio<=0.30):
        respuesta = 8
    elif(aleatorio<=0.60):
        respuesta = 9
    else: 
        respuesta = 10
    return respuesta