# Ugalde Carreño Paulina 19141209
# Algoritmo Congruencial Aditivo para una suseción de números enteros

# ------------------------------------------------------------
# DECLARACION DE VARIABLES GLOBALES
# Declaramos nuestras matrices vacias
x = []
r = []

no_datos = 100

# Agregamos 0 a nuestros vectores
for i in range(no_datos):                
    x.append(0)
    r.append(0)

# Abrimos nuestro archivo txt donde vamos a almacenar nuestros resultados
File = open("Resultados.txt", "w")
# ------------------------------------------------------------

# ------------------------------------------------------------
# Pedimos los datos por consola
# 1. Ingrese los datos:
# semilla - x0
cantidad = int(input("Ingresa la cantidad de datos a ingresar: "))
for i in range(cantidad):
    x[i] = int(input("Dato "+str(i+1)+": "))
#  variables
m = int(input("Ingresa el valor de m: "))
# ------------------------------------------------------------

def formarX(x1, x2):
    resultado = (x1+x2)%m
    return resultado

def calcularR(x):
    resultado = x/(m-1)
    return resultado

# Debemos formar la tabla
def formarTabla():
    aux = 0
    for i in range(cantidad, no_datos, 1):
        x[i] = formarX(x[i-1], x[aux])
        r[i] = calcularR(x[i])
        aux += 1

def imprimirResultados():
    File.write("Cantidad de datos ingresados: "+str(cantidad)+" -----------------------------------------------------------\n")
    File.write("m: "+str(m)+" -----------------------------------------------------------\n")
    
    for i in range(no_datos):
        File.write("x"+str(i+1)+": "+str(x[i])+"\t\tr"+str(i+1)+": "+str(round(r[i],4))+"\n")
    File.close()  

# ------------------------------------------------------------
# Mandamos a llamar a nuestros métodos
formarTabla()
imprimirResultados()