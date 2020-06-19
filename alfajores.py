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
intervaloLlegada=random.normalvariate(69.42, 10.17)
#saltamos siempre al evento mas proximo
while(tiempo<=3600):
    print ('=================nueva iteracion ===================')
       
    print('-------------tiempo inicial------: ' + str(tiempo))
    # lo proximo que viene es una llegada
    if (tiempo + intervaloLlegada) < (tiempo + tiempoArmado) and (tiempo+intervaloLlegada <(tiempo+tiempoBanio)):
        print('Llegada de Tapa')
        #Llega una tapa primero
        tiempo += intervaloLlegada
        intervaloLlegada=random.normalvariate(69.42, 10.17)
        alfajoresxdia+=1
        
        if(armadoLibre):
            print('Inicia Armado')
        # ARMADO LIBRE 
            tiempoArmado = random.normalvariate(64.56, 10.025)
            armadoLibre= False
            
            # media y varianza 
            
        else:
            print('Se aniade tapa a cola armado')
            colaArmado +=1


    elif ((tiempo + tiempoArmado) < (tiempo + tiempoBanio)):
    #PROCESO DE ARMADO  
        print('Armado')
        tiempo += tiempoArmado
        if(banioLibre):
            print('Banio esta libre, alfajor pasa de armado a banio')
            # BANIADO LIBRE 
            armadoLibre = True
            banioLibre = False
            tiempoBanio = random.normalvariate(64.76, 5)
            if(colaArmado > 0 ):
                print('Cola de Armado con elementos, tomo uno para continuar armando')
                armadoLibre = False
                colaArmado -= 1
                tiempoArmado = random.normalvariate(64.56, 10.025)
            
            else:
                print('La cola esta vacia, armado queda Libre')
                tiempoArmado = sys.maxsize
                
        else:
            print('Banio ocupado: el armado espera con el alfajor')
            armadoEspera = True
            armadoLibre = False
    else:
        print('Baniado')
    #procesar un baniado
        tiempo += tiempoBanio
        if(armadoEspera):
            print('Baniado toma el alfajor de armado')
            armadoEspera = False
            banioLibre = False
            tiempoBanio = random.normalvariate(64.76, 5)
        else:
            print('Armado no tiene nada, Banio descansa')
            banioLibre = True
        
        #CONTROL DE CALIDAD EL COMUNMENTE CONOCIDO -QA-
        evaluacion = random.randint(0,101)
        if(evaluacion<=90):
            admitidos +=1
        else:
            perdida +=1 


    
    
    print('-------------tiempo final------: ' + str(tiempo))
    print('Armado:' + str(tiempo + tiempoArmado))
    print('Baniado:' + str(tiempo + tiempoBanio))
    print('intervalo llegada prox:' + str(tiempo+intervaloLlegada)) 
    print("Perdidos: " + str(perdida))
    print("Admitidos: " + str(admitidos))
    print("alfajores potenciales para armar: " + str(alfajoresxdia))
    print("Cola del armados: "+ str(colaArmado))