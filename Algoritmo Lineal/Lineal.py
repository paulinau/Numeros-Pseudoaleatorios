# Ugalde Carreño Paulina 19141209
# Algoritmo de Multiplicador Constante

# ------------------------------------------------------------
# DECLARACION DE VARIABLES GLOBALES
# Declaramos nuestras matrices vacias
x = []
r = []

# Abrimos nuestro archivo txt donde vamos a almacenar nuestros resultados
File = open("Resultados.txt", "w")
# ------------------------------------------------------------

# ------------------------------------------------------------
# Pedimos los datos por consola
# 1. Ingrese los datos:
# semilla - x0
x0 = int(input("Ingresa el valor de x0: "))
#  variables
g = int(input("Ingresa el valor de g: "))
k = int(input("Ingresa el valor de k: "))
# constante aditiva - c (relativamente primo a m)
c = int(input("Ingresa el valor de c: "))
# ------------------------------------------------------------

# ------------------------------------------------------------
# Realizamos los respectivos calculos
# constante multiplicativa - a
a = 1+4*k
# modulo - m (periodo de vida maximo)
m = pow(2,g)
# ------------------------------------------------------------

# ------------------------------------------------------------
# Definicion de metodos
# Agregamos 0 a nuestros vectores
for i in range(m):                
    x.append(0)
    r.append(0)

def formarX(x):
    resultado = (a*x+c)%m
    return resultado

def calcularR(x):
    resultado = x/(m-1)
    return resultado

# Debemos formar la tabla
def formarTabla():
    for i in range(m):
        # La "x" de la primer fila la formamos por separado
        # Para la primera fila:
        if (i == 0):
            x[i] = formarX(x0)
        # Las demas filas las formamos todas juntas
        else:
            x[i] = formarX(x[i-1])
        
        # Calculamos los demas valores
        r[i] = calcularR(x[i])

def imprimirResultados():
    File.write("X0: "+str(x0)+" -----------------------------------------------------------\n")
    File.write("a: "+str(a)+" -----------------------------------------------------------\n")
    File.write("c: "+str(c)+" -----------------------------------------------------------\n")
    File.write("m: "+str(m)+" -----------------------------------------------------------\n")
    File.write("g: "+str(g)+" -----------------------------------------------------------\n")
    File.write("k: "+str(k)+" -----------------------------------------------------------\n")
    for i in range(m):
        File.write("x"+str(i+1)+": "+str(x[i])+"\tr"+str(i+1)+": "+str(round(r[i],4))+"\n")  
    File.close()
# ------------------------------------------------------------

# ------------------------------------------------------------
# Mandamos a llamar a nuestros métodos
formarTabla()
imprimirResultados()