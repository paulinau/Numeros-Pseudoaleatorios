# Ugalde Carreño Paulina 19141209
# Algoritmo de Productos Medios

# ------------------------------------------------------------
# DECLARACION DE VARIABLES GLOBALES
# Declaramos nuestras matrices vacias
y = []
ceros = []
x = []
r = []
duplicados = []
R = []

# Abrimos nuestro archivo txt donde vamos a almacenar nuestros resultados
File = open("Resultados.txt", "w")

# Definimos una constante, es decir, el número de numeros maximo que se pueden crear
#filas = 499
# ------------------------------------------------------------

# ------------------------------------------------------------
# Pedimos los datos por consola
# 1. Ingrese dos numeros de 4 digitos
x0 = int(input("Ingresa el valor de x0: "))
x1 = int(input("Ingresa el valor de x1: "))
# Extra: Ingresamos el numero de numeros que vamos a calcular
filas = int(input("Cantidad de numeros pseudoaleatorios a calcular: "))
# ------------------------------------------------------------

# ------------------------------------------------------------
# Definicion de metodos
# Agregamos 0 a nuestros vectores
for i in range(filas):            
    y.append(0)      
    ceros.append(0)
    x.append(0)
    r.append(0)

# 2. Agregue 0 del lado izquierdo con el fin de contar 8 digitos
def validarDigitos(mult):
    aux = ""
    longitud = len(str(mult))
    for i in range(longitud, 8, 1):
        aux = "0" + aux
    final = aux + str(mult)
    return final

# 3. Seleecione los cuatro digitos centrales
def digitosCentrales(mult):
    rango = slice(2,6)
    no_8digits = validarDigitos(mult)[rango]
    return no_8digits

# 4. Sacar r
def calcularR(x):
    r2 = x/10000
    return r2

# Repetir los pasos 3 y 4
# Debemos formar la tabla
def formarTabla():
    for i in range(filas):
        # La "y" de la primer y segunda fila la formamos por separado
        # Para la primera fila:
        if (i == 0):
            y[i] = x0*x1
        # Para la segunda fila
        elif (i==1):
            y[i] = x1*int(x[i-1])
        # Para las filas posteriores
        else:
            y[i] = int(x[i-2])*int(x[i-1])
        
        # Calculamos los demas valores (incluyendo duplicados)
        ceros[i] = validarDigitos(y[i])
        x[i] = digitosCentrales(ceros[i])
        r[i] = float(calcularR(int(x[i])))

#Checamos los numeros duplicados
def dup(r):
    for i in r:
        if i in R:
            # Si es el mismo numero, se ira a duplicados
            duplicados.append(i)
            R.append("a")
        else:
            # Sino, se pasará a R
            R.append(i)
            duplicados.append("a")

def imprimirVectores():
    longitud = len(R)
    longitud2 = len(duplicados)

    File.write("X0: "+str(x0)+"-----------------------------------------------------------\n")
    File.write("X1: "+str(x1)+"-----------------------------------------------------------\n")
    for i in range(longitud):
        if(str(R[i]) != "a"):
            if(len(str(y[i])) < 7):
                File.write("y"+str(i)+": "+str(y[i])+"\t\t"+str(ceros[i])+"\t\tx"+str(i+2)+": "+str(x[i])+"\tr"+str(i+1)+": "+str(R[i])+"\n")
            else:
                File.write("y"+str(i)+": "+str(y[i])+"\t"+str(ceros[i])+"\t\tx"+str(i+2)+": "+str(x[i])+"\tr"+str(i+1)+": "+str(R[i])+"\n")
    File.write("================================ VALORES DUPLICADOS =================================\n")
    for i in range(longitud2):
        if(str(duplicados[i]) != "a"):
            if(len(str(y[i])) < 6):
                File.write("y"+str(i)+": "+str(y[i])+"\t\t\t"+str(ceros[i])+"\t\tx"+str(i+2)+": "+str(x[i])+"\tr"+str(i+1)+": "+str(duplicados[i])+"\n")
            else:
                File.write("y"+str(i)+": "+str(y[i])+"\t"+str(ceros[i])+"\t\tx"+str(i+2)+": "+str(x[i])+"\tr"+str(i+1)+": "+str(duplicados[i])+"\n")
    File.close()
# ------------------------------------------------------------
# Mandamos a llamar a nuestros métodos
formarTabla()
dup(r)
imprimirVectores()