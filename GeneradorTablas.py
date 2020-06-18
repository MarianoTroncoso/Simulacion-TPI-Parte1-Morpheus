import random
import csv
"""
#Genera mediciones del tiempo que toma hacer el alfajor
with open('hacerAlfajores.csv', mode = 'w') as hacerAlfajores:
    alfajores_writer = csv.writer(hacerAlfajores, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    n = 0
    while n < 1000:
        val = random.normalvariate(55,10)
        print(val)
        alfajores_writer.writerow([val])
        n+=1

with open('aprobacionControlCalidad.csv',mode = 'w') as controlCalidad:
    control_writer = csv.writer(controlCalidad,delimiter = ',',quotechar = '"',quoting= csv.QUOTE_MINIMAL)
  
    for i in range(0,1000):
        if random.random() < 0.95:
            val="Aprobado"
            val2=1
        else:
            val= "Rechazado"
            val2=0
        print(val2)
        control_writer.writerow([val])     
"""
"""
with open('tiempoBañado.csv',mode = 'w') as tiempoBañado:
     bañado_writer = csv.writer(tiempoBañado,delimiter =',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
     for i in range(0,1000):
        val = random.normalvariate(65,5)
        print(round(val,2))
        bañado_writer.writerow([val])

"""
with open('intervaloLlegada.csv',mode ='w') as intervaloLlegada:
    intervaloLlegada_writer = csv.writer(intervaloLlegada,delimiter =',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
    for i in range(0,1000):
        val = random.normalvariate(70,10)
        print(round(val,2))
        intervaloLlegada_writer.writerow([val])
