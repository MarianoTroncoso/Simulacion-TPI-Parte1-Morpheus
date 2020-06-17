from pruebaFalsa import *
import random

def GeneraLugar2():
    aleatorio = 0
    respuesta=''
    aleatorio = random.random()
    if (aleatorio<=0.3):
        respuesta=1
    elif (aleatorio<=0.6):
        respuesta=2
    else:
        respuesta=3

    return respuesta

# Codigo simulacion

# Tiempo de procesamiento
def GeneraTiempo():
    a = 1
    b = 5 
    ri = random.random()
    return round(( a + (b - a) * ri),2)
     
# Destino de los paquetes
def GeneraLugar():
    
    valorGenerado = random.roundrange(0,3)
    if valorGenerado == 0:
        return 'A';
    elif valorGenerado == 1:
        return 'B';
    else:
        return 'C'

# Intervalo entre arribos 
#def GeneraSiguiente():
    
    
def ImprimirEstadoTerminal():
    print("A: "+str(estadoTerminalA)+" TiempoRemanente "+str(tiempoRemanenteA))
    print("B: "+str(estadoTerminalB)+" TiempoRemanente "+str(tiempoRemanenteB))
    print("C: "+str(estadoTerminalC)+" TiempoRemanente "+str(tiempoRemanenteC))

def ImprimirMemoria():
    print("A: "+ "MemoriaRouter "+str(memoriaRouterA))
    print("B: "+ "MemoriaRouter "+str(memoriaRouterB))
    print("C: "+ "MemoriaRouter "+str(memoriaRouterC))

def ImprimirTiempoProcesamiento():
    print("A: "+ "Tiempo Procesamiento "+str(tiempoProcMemoriaA))
    print("B: "+ "Tiempo Procesamiento "+str(tiempoProcMemoriaB))
    print("C: "+ "Tiempo Procesamiento "+str(tiempoProcMemoriaC))
    

    
intervaloLlegada = 0

estadoTerminalA = False
estadoTerminalB = False
estadoTerminalC = False

tiempoRemanenteA = 0
tiempoRemanenteB = 0
tiempoRemanenteC = 0

memoriaRouterA = False
memoriaRouterB = False
memoriaRouterC = False

#tiempo de procesamiento de los paquetes de la memoria del Router
tiempoProcMemoriaA = 0
tiempoProcMemoriaB = 0
tiempoProcMemoriaC = 0

#paquetes perdidos
paquetesPerdidos = 0
paquetesProcesados = 0
porcentajePerdidos = 0

condicion = True
tiempo = 0
paquete = 0
while condicion:
    #Actualizar tiempos
    # Never, never do this 
    if (intervaloLlegada) < (tiempoRemanenteA) and (intervaloLlegada) < (tiempoRemanenteB) and (intervaloLlegada) < (tiempoRemanenteC):
        paquete+=1
        tiempo = intervaloLlegada
        #Tenemos que procesar una llegada
        procesamientoPaqueteActual= tiempo + GeneraTiempo2() 
        destinoPaqueteActual = tiempo + GeneraLugar2() #aleatorioEncabezado
        intervaloLlegada = tiempo + GeneraSiguiente2()

        if procesamientoPaqueteActual == 'A': #terminalA
            if estadoTerminalA == False:
                estadoTerminalA = True
                tiempoRemanenteA = procesamientoPaqueteActual
            else:
                #La terminal esta ocupada, comprobamos la memoria del router
                if memoriaRouterA == True:
                    #Paquete se pierde
                    paquetesPerdidos +=1
                else:
                    memoriaRouterA = True
                    tiempoProcMemoriaA = procesamientoPaqueteActual  

        if procesamientoPaqueteActual == 'B': #terminalB
            if estadoTerminalB == False:
                estadoTerminalB = True
                tiempoRemanenteB = procesamientoPaqueteActual
            else:
                #terminal ocupada, compruebo memoria
                if memoriaRouterB == True:
                    #paquete se pierde
                    paquetesPerdidos +=1
                else:
                    #cargo en memoria
                    memoriaRouterB = True
                    tiempoProcMemoriaB = procesamientoPaqueteActual
                    

        if procesamientoPaqueteActual == 'C': #terminalC
            if estadoTerminalC == False:
                estadoTerminalC = True
                tiempoRemanenteC = procesamientoPaqueteActual
            else:
                #terminal ocupada, compruebo memoria
                if memoriaRouterC == True:
                    #paquete se pierde
                    paquetesPerdidos +=1
                else:
                    memoriaRouterC = True
                    tiempoProcMemoriaC = procesamientoPaqueteActual

        porcentajePerdidos = paquetesPerdidos*100/paquete
        #perdida de un paquechi
    else:
        #Se procesa una salida        
        #Primero, liberamos las terminales y  Liberamos la memoria del router
        tiempo = min(tiempoRemanenteA,tiempoRemanenteB,tiempoRemanenteC)

       
        if tiempo == tiempoRemanenteA and estadoTerminalA:
            estadoTerminalA = False
            if memoriaRouterA:
                estadoTerminalA = True
                tiempoRemanenteA = tiempoProcMemoriaA
                memoriaRouterA = False
        if tiempo == tiempoRemanenteB and estadoTerminalB:
            estadoTerminalB = False
            if memoriaRouterB:
                estadoTerminalB = True
                tiempoRemanenteB = tiempoProcMemoriaB
                memoriaRouterB = False
        if tiempo == tiempoRemanenteC and estadoTerminalC:
            estadoTerminalC = False
            if memoriaRouterC:
                estadoTerminalC = True
                tiempoRemanenteC = tiempoProcMemoriaB
                memoriaRouterC = False
    ImprimirEstadoTerminal()
    ImprimirMemoria()
    ImprimirTiempoProcesamiento()
    if paquete == 20:
        condicion = False


    
    


    
    
    
    

