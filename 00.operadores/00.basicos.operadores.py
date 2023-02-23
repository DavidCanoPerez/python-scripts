# -*- coding: utf-8 -*-


""" ---------------------------------------------------------------------------------
    operadores aritmeticos basicos
        suma
        resta
        multiplicacion
        division con salida entera
"""

print("-------- operadores aritmeticos basicos")

suma = 2 + 2
resta = 2 - 1
multiplicacion = 2 * 3

division = 3 // 2               # division con resultado entero         
print("division entera: " + str(division))


""" ---------------------------------------------------------------------------------
    otros operadores aritmeticos
        cambio signo
        exponente
        division con salida decimal
"""

print("-------- otros operadores aritmeticos")

cambio_signo1 = 5
cambio_signo2 = -cambio_signo1
print("cambio signo = ", cambio_signo2)

print("exponente = ", 2**2)
print("division =", 1/2)        # division con resultado decimal
print("operador de modulo, residuo o resto", 1%2)


""" ---------------------------------------------------------------------------------
    reglas prioridad operaciones
        parentesis
        exponente
        multiplicacion
        division
        suma
        sustraccion
"""

print("-------- reglas prioridad operaciones")

resultado1 = 10 * 2 - 2
print(f"resultado1 = {resultado1}")
resultado2 = 10 * (5 - 2)
print(f"resultado2 = {resultado2}")
resultado3 = 10 * 2 ** 3 
print(f"resultado3 = {resultado3}")
resultado4 = (10 * 2) ** 3
print(f"resultado4 = {resultado4}")


""" ---------------------------------------------------------------------------------
    operadores relacionales
        ==	iguales
        !=	distintos
        >	mayor que
        <	menor que
        >=	mayor o igual que
        <=	menor o igual que
"""

print("-------- operadores relacionales")

variable = 1
while variable <= 10:
    variable +=1
print("valor de variable es", variable)

""" ---------------------------------------------------------------------------------
    operadores logicos
        or
        and
        not
"""

print("-------- operadores logicos")

a = 1
b = 2
c = 3
if a < b or b < c:
  print("a o b son menores que c")

if c > a and c > b:
  print("c es mayor que a y que b")
  
""" ---------------------------------------------------------------------------------
    operadores de pertenencia
        in 
        not in
                    devuelven un valor boleano
"""

print("-------- operadores de pertenencia")

# ejemplo con cadena
cadena = "hola"
bool_data = "h" in cadena
bool_not_data = "h" not in cadena
print("pertenecia cadena", bool_data)          # True
print("pertenecia cadena not", bool_not_data)  # False

# ejemplo caracter en cadena
s = "myweb.com"
ch_illegal = "."
if ch_illegal in s:
     print("Character found")
else:
    print("Character not found")

# ejemplo no relacionado pero mas ajustado que el anterior
s = "myweb.com"
ch_illegal = "/"
if s.find(ch_illegal) != -1:
    print("Character found")
else:
    print("Character not found")

# ejemplo con lista
nombres = ["Daniel", "Juan", "Olga"]
if "Olga" in nombres:
  print("El nombre Olga esta en la lista")


""" ---------------------------------------------------------------------------------
    operadores de identidad
        is
        is not
"""

print("-------- operadores de identidad")

cadena2 = "Hola mundo"
numero2 = 2
f = 1.23

# cuidado esto no funciona
if cadena2 is str:
    print("cadena2 es tipo string")
    # no se imprime
else:
    print("no se imprime")

# cuidado esto no funciona
print("será erroneo, cadena2 es string:", cadena2 is str)
print("será erroneo, numero2 es entero:", numero2 is not int)

# si funciona
bool_234 = isinstance(cadena2, str)
print("será correcto que cadena2 es string:", bool_234)

bool_45 = isinstance(numero2, int)
print("será correcto que cadena2 es int:", bool_45)

bool_456 = isinstance(f, float)
print("será correcto que cadena2 es float:", bool_456)

if bool_234 & bool_45 & bool_456 == True:
    print("todo funciona")


""" ---------------------------------------------------------------------------------
    operadores de asignacion
        =	asignacion
        +=	suma
        -=	resta
        *=	multiplicación
        **=	exponencia
        /=	división
        //=	division (valor entero)
        %=	modulo, residuo, resto (división)
"""

print("-------- operadores de asignacion")

x = 10
y = x
x -=1       # cuidado si esta linea fuera x =-1 entonces x valdra -1
print("valor de z es ", x)


""" ---------------------------------------------------------------------------------
    operadores a nivel bit
        &	AND
        |	OR
        ^	XOR
        <<	desplazar bits a la izquierda
        >>	desplazar bits a la derecha
"""





