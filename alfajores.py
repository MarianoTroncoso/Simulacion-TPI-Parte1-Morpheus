import random

segundo=0
alfajoresxdia = 0
dias = 0
tiempoArmado= 0         #entre 40 y 70
tiempoBanio = 0   #entre 50 y 80
evaluacion = 0    #aleatorio para ver si pasa la prueba
ganancia = 0
admitidos= 0
perdida = 0
armadoOcupado = False
banioOcupado = False
intervaloLlegada = 0
colaArmado = 0

while(segundo<=10400):
    intervaloLlegada=random.randint(50,90)
    
    if(armadoOcupado==False):
        
        alfajoresxdia+=1
        armadoOcupado= True
        
        tiempoArmado = random.randint(40,71)
        segundo += tiempoArmado
        
        if(banioOcupado == False):
            
            armadoOcupado = False
            banioOcupado=True
            tiempobanio = random.randint(80,121)
            segundo += tiempoBanio
            banioOcupado = False
            evaluacion =random.randint(0,101)
            if(evaluacion<=90):
                admitidos +=1
            else:
                perdida +=1 
    
    #ARMADO OCUPADO            
    else:
        colaArmado +=1
        segundo = segundo + intervaloLlegada
        if(segundo>tiempoArmado):
            alfajoresxdia+=1
            armadoOcupado= True
        
            tiempoArmado = random.randint(40,71)
            segundo += tiempoArmado
            colaArmado-=1
        
            if(banioOcupado == False):
                
                armadoOcupado = False
                banioOcupado=True
                tiempobanio = random.randint(80,121)
                segundo += tiempoBanio
                banioOcupado = False
                evaluacion =random.randint(0,101)
                if(evaluacion<=90):
                    admitidos +=1
                else:
                    perdida +=1 


print("Perdidos: " + str(perdida))
print("Admitidos: " + str(admitidos))
print("Procesados: " + str(alfajoresxdia))
print(colaArmado)