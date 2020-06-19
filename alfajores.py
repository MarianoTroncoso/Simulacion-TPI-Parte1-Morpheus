import random
import sys
tiempo=0
alfajoresxdia = 0
dias = 0
tiempoArmado= sys.maxsize       #entre 40 y 70
tiempoBanio = sys.maxsize    #entre 50 y 80
evaluacion = 0    #aleatorio para ver si pasa la prueba
ganancia = 0
admitidos= 0
perdida = 0
armadoLibre = False
banioLibre = False
intervaloLlegada = 0
colaArmado = 0
armadoEspera = False

#saltamos siempre al evento mas proximo
while(tiempo<=3600):
    print('-------------tiempo: ' + str(tiempo))
    # lo proximo que viene es una llegada
    if (tiempo + intervaloLlegada) < (tiempo + tiempoArmado) and (tiempo+intervaloLlegada <(tiempo+tiempoBanio)):
        print('LLEGO UNA TAPA CALIENTITA')
        #Llega una tapa primero
        tiempo += intervaloLlegada
        intervaloLlegada=random.normalvariate(69.42, 10.17)
        alfajoresxdia+=1
        
        if(armadoLibre==True):
        # ARMADO LIBRE 
            tiempoArmado = random.normalvariate(64.56, 10.025)
            armadoLibre= False
            
            # media y varianza 
            
        else:
            colaArmado +=1


    elif ((tiempo + tiempoArmado) < (tiempo + tiempoBanio)):
    #PROCESO DE ARMADO  
        tiempo += tiempoArmado
        if(banioLibre == True):
            # BANIADO LIBRE 
            armadoLibre = True
            banioLibre = False
            tiempobanio = random.normalvariate(64.76, 5)
            if(colaArmado > 0 ):
                armadoLibre = False
                colaArmado -= 1
                tiempoArmado = random.normalvariate(64.56, 10.025)
            
            else:
                tiempoArmado = sys.maxsize
                
        else:
            armadoEspera = True
    else:
    #procesar un baniado
        tiempo += tiempoBanio
        if(armadoEspera):
            armadoEspera = False
            banioLibre = False
            tiempobanio = random.normalvariate(64.76, 5)
        else:
            banioLibre = True
        
        #CONTROL DE CALIDAD EL COMUNMENTE CONOCIDO -QA-
        evaluacion = random.randint(0,101)
        if(evaluacion<=90):
            admitidos +=1
        else:
            perdida +=1 


    


    print("Perdidos: " + str(perdida))
    print("Admitidos: " + str(admitidos))
    print("Procesados: " + str(alfajoresxdia))
    print(colaArmado)