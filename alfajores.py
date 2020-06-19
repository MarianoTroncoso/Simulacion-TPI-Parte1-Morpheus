import random

tiempo=0
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

#saltamos siempre al evento mas proximo
while(tiempo<=3600):
    # lo proximo que viene es una llegada?
    if (tiempo + intervaloLlegada) < (tiempo + tiempoArmado) and (tiempo+intervaloLlegada <(tiempo+tiempoBanio)):
        #Llega una tapa primero
    intervaloLlegada=random.randint(50,90)
    
    if(armadoOcupado==False):
        # ARMADO LIBRE 
        alfajoresxdia+=1
        armadoOcupado= True
        
        # media y varianza 
        tiempoArmado = random.normalvariate(64.56,10.025)
        # saltamos hasta que se termina de armar el alfajor
        tiempo += tiempoArmado
        
        if(banioOcupado == False):
            # BAÑADO LIBRE 
            armadoOcupado = False
            banioOcupado=True
            tiempobanio = random.randint(80,121)
            tiempo += tiempoBanio
            banioOcupado = False
            evaluacion =random.randint(0,101)
            if(evaluacion<=90):
                admitidos +=1
            else:
                perdida +=1 
    
    #ARMADO OCUPADO            
    else:
        colaArmado +=1
        tiempo = tiempo + intervaloLlegada
        if(tiempo>tiempoArmado):
            alfajoresxdia+=1
            armadoOcupado= True
        
            tiempoArmado = random.randint(40,71)
            tiempo += tiempoArmado
            colaArmado-=1
        
            if(banioOcupado == False):
                
                armadoOcupado = False
                banioOcupado=True
                tiempobanio = random.randint(80,121)
                tiempo += tiempoBanio
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