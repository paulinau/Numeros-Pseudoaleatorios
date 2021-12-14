# Ugalde Carreño Paulina 19141209
# Algoritmo de Cuadrados medios Von Neumann

# ------------------------------------------------------------
# DECLARACION DE VARIABLES GLOBALES
# Declaramos nuestras matrices vacias
cuadrados = []
ceros = []
x = []
r = []
duplicados = []
R = []

# Abrimos nuestro archivo txt donde vamos a almacenar nuestros resultados
File = open("Resultados.txt", "w")

# Definimos una constante, es decir, el número de numeros maximo que se pueden crear
#filas = 100
# ------------------------------------------------------------

# ------------------------------------------------------------
# Pedimos los datos por consola
# 1. Ingrese un numero de 4 digitos
numero = int(input("Ingresa el valor de x0: "))
# Extra: Ingresamos el numero de numeros que vamos a calcular
filas = int(input("Cantidad de numeros pseudoaleatorios a calcular: "))
# ------------------------------------------------------------

# ------------------------------------------------------------
# Definicion de metodos
# Agregamos 0 a nuestros vectores
for i in range(filas):            
    cuadrados.append(0)      
    ceros.append(0)
    x.append(0)
    r.append(0)

# 2. Eleve al cuadraro dicho numero
def elevarCuadrado(numero):
    cuadrado = pow(numero,2)
    return cuadrado

# 3. Agregue 0 del lado izquierdo con el fin de contar 8 digitos
def validarDigitos(cuadrado):
    aux = ""
    longitud = len(str(cuadrado))
    for i in range(longitud, 8, 1):
        aux = "0" + aux
    final = aux + str(cuadrado)
    return final

# 4. Seleecione los cuatro digitos centrales
def digitosCentrales(cuadrado):
    rango = slice(2,6)
    no_8digits = validarDigitos(cuadrado)[rango]
    return no_8digits

# 5. Sacar r
def calcularR(x):
    r2 = x/10000
    return r2

# Repetir los pasos 3 y 4
# Debemos formar la tabla
def formarTabla():
    for i in range(filas):
        # La primera fila la formamos por separado
        if(i == 0):
            cuadrados[i] = numero
            ceros[i] = validarDigitos(numero)
            x[i] = numero
            r[i] = numero/10000
        # Formamos las demas filas (con todo y duplicados)
        else:
            cuadrados[i] = elevarCuadrado(int(x[i-1]))
            ceros[i] = validarDigitos(cuadrados[i])
            x[i] = digitosCentrales(ceros[i])
            r[i] = float(calcularR(int(x[i])))

#Checamos los numeros duplicados
def dup(r):
    for i in r:
        if i in R:
            # Si es el mismo numero, se ira a duplicados
            duplicados.append(i)
        else:
            # Sino, se pasará a R
            R.append(i)

def imprimirResultados():
    longitud = len(R)
    longitud2 = len(duplicados)

    File.write("X0: "+str(numero)+"-----------------------------------------------------------\n")
    for i in range(longitud):
        if(len(str(cuadrados[i])) < 8):
            File.write(str(cuadrados[i])+"\t\t"+str(ceros[i])+"\t\tx"+str(i)+": "+str(x[i])+"\tr"+str(i)+": "+str(R[i])+"\n")
        else:
            File.write(str(cuadrados[i])+"\t"+str(ceros[i])+"\t\tx"+str(i)+": "+str(x[i])+"\tr"+str(i)+": "+str(R[i])+"\n")
    File.write("================================= VALORES DUPLICADOS =================================\n")
    for i in range(longitud2):
        if(len(str(cuadrados[longitud+i])) < 8):
            File.write(str(cuadrados[longitud+i])+"\t\t"+str(ceros[longitud+i])+"\t\tx"+str(longitud+i)+": "+str(x[longitud+i])+"\tr"+str(longitud+i)+": "+str(duplicados[i])+"\n")
        else:
            File.write(str(cuadrados[longitud+i])+"\t"+str(ceros[longitud+i])+"\t\tx"+str(longitud+i)+": "+str(x[longitud+i])+"\tr"+str(longitud+i)+": "+str(duplicados[i])+"\n")
    File.close()
# ------------------------------------------------------------



# ------------------------------------------------------------
# Mandamos a llamar a nuestros métodos
formarTabla()
dup(r)
imprimirResultados()
# ------------------------------------------------------------
