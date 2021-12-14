# Ugalde Carreño Paulina 19141209
# Algoritmo Congruencial Multiplicativo

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
# ------------------------------------------------------------

# ------------------------------------------------------------
# Realizamos los respectivos calculos
# constante multiplicativa - a
a = 3+8*(k)
# modulo - m
m = pow(2,g)
# periodo de vida maximo - N
N = pow(2,g-2)
# ------------------------------------------------------------

# ------------------------------------------------------------
# Definicion de metodos
# Agregamos 0 a nuestros vectores
for i in range(N):                
    x.append(0)
    r.append(0)

def formarX(x):
    resultado = (a*x)%m
    return resultado

def calcularR(x):
    resultado = x/(m-1)
    return resultado

# Debemos formar la tabla
def formarTabla():
    for i in range(N):
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
    File.write("N: "+str(N)+" -----------------------------------------------------------\n")
    File.write("m: "+str(m)+" -----------------------------------------------------------\n")
    File.write("g: "+str(g)+" -----------------------------------------------------------\n")
    File.write("k: "+str(k)+" -----------------------------------------------------------\n")
    for i in range(N):
        if(len(str(x[i]))>2):
            File.write("x"+str(i+1)+": "+str(x[i])+"\tr"+str(i+1)+": "+str(round(r[i],4))+"\n")
        else:    
            File.write("x"+str(i+1)+": "+str(x[i])+"\t\tr"+str(i+1)+": "+str(round(r[i],4))+"\n")
    File.close()

# ------------------------------------------------------------
# Mandamos a llamar a nuestros métodos
formarTabla()
imprimirResultados()