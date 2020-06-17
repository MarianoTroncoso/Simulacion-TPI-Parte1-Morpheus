import random   

# Tiempo de procesamiento
def GeneraTiempoBobo():
    a = 1
    b = 5 
    ri = random.random()
    return round(( a + (b - a) * ri),2)

# Tiempo de procesamiento
#def GeneraTiempoUniform():
    
   # return round(random.uniform(0,5),2)

print(GeneraTiempoBobo())
print(GeneraTiempoBobo())
print(GeneraTiempoBobo())
print(GeneraTiempoBobo())
print(GeneraTiempoBobo())
