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
armadoLibre = True
banioLibre = True
intervaloLlegada = 0
colaArmado = 0
armadoEspera = False

#saltamos siempre al evento mas proximo
while(tiempo<=1000):
    print ('=================nueva iteracion ===================')
    print('armado:' + str(tiempoArmado))
    print('baniado:' + str(tiempoBanio))
    print('intervalo llegada prox:' + str(intervaloLlegada))    
    print('-------------tiempo inicial------: ' + str(tiempo))
    # lo proximo que viene es una llegada
    if (tiempo + intervaloLlegada) < (tiempo + tiempoArmado) and (tiempo+intervaloLlegada <(tiempo+tiempoBanio)):
        print('===============LLEGADA DE UNA TAPA CALIENTITA =============')
        #Llega una tapa primero
        tiempo += intervaloLlegada
        intervaloLlegada=random.normalvariate(69.42, 10.17)
        alfajoresxdia+=1
        
        if(armadoLibre):
            print('entro a un armado libre 1')
        # ARMADO LIBRE 
            tiempoArmado = random.normalvariate(64.56, 10.025)
            armadoLibre= False
            
            # media y varianza 
            
        else:
            print('sumo a cola armado')
            colaArmado +=1


    elif ((tiempo + tiempoArmado) < (tiempo + tiempoBanio)):
    #PROCESO DE ARMADO  
        print( 'soy un control de bugs (.)(.)()(.)(.)()()()()()() ')
        tiempo += tiempoArmado
        if(banioLibre):
            print('soy un banio libre')
            # BANIADO LIBRE 
            armadoLibre = True
            banioLibre = False
            tiempobanio = random.normalvariate(64.76, 5)
            if(colaArmado > 0 ):
                print('hay cosas en cola y el armado saca 1')
                armadoLibre = False
                colaArmado -= 1
                tiempoArmado = random.normalvariate(64.56, 10.025)
            
            else:
                print('la cola vacia tiempo armado infinito')
                tiempoArmado = sys.maxsize
                
        else:
            print('banio ocupado el armado espera con el alfajor')
            armadoEspera = True
    else:
        print('PROCESO BANIO HA INICIADO')
    #procesar un baniado
        tiempo += tiempoBanio
        if(armadoEspera or armadoLibre):
            
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


    
    
    print('-------------tiempo final------: ' + str(tiempo))

    print("Perdidos: " + str(perdida))
    print("Admitidos: " + str(admitidos))
    print("alfajores potenciales para armar: " + str(alfajoresxdia))
    print("Cola del armados: "+ str(colaArmado))