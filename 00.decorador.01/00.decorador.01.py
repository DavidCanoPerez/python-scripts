# -*- coding: utf-8 -*-

"""
    decoradores @
        aunque se denominan decoradores no son comentarios
        permitía modificar funciones y métodos, actualmente también clases
            por eso se hace dificil entender y sintetizar su potencial
        generalmente, alteran de forma versatil y dinámica la funcionalidad
            son empleados en depuración avanzada, control... 
        la funcionalidad es uno de los puntos más cuidados y fuertes de python
    
    documentación general
        https://wiki.python.org/moin/PythonDecorators
        https://peps.python.org/pep-0318/
    @property
        https://docs.python.org/es/3/library/functions.html#property
    @staticmethod  
        https://docs.python.org/es/3/library/functions.html#staticmethod
    @classmethod    
        https://docs.python.org/es/3/library/functions.html#classmethod
    @override
        https://docs.python.org/es/3/whatsnew/3.12.html#pep-698-override-decorator-for-static-typing
    
"""

#-----------------------------------------------------------------------------------------
# ejemplo1
#       @foo
#       decorador de función
#-----------------------------------------------------------------------------------------

# definición decorador
def decorador(funcion):
    def wrapper():
        print("Antes de llamar a la función")
        funcion()
        print("Después de llamar a la función")
    return wrapper

@decorador    # decorador para modificar a la función saludo
def saludo():
    print("¡Hola, mundo!")

print("----Ejemplo1")
saludo()    # llamada a función decorada


#-----------------------------------------------------------------------------------------
# ejemplo2
#       @property        
#       uso común de decorador @property para métodos (getter y setter) como propiedades
#-----------------------------------------------------------------------------------------

class Contacto:
    def __init__(self, id, nombre, apellido1, apellido2, telefono, notas=""):
        self._id = id
        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._telefono = telefono
        self._notas = notas

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido1(self):
        return self._apellido1

    @property
    def apellido2(self):
        return self._apellido2

    @property
    def telefono(self):
        return self._telefono

    @property
    def notas(self):
        return self._notas

    @notas.setter
    def notas(self, valor):
        self._notas = valor

print("----Ejemplo2")

# crear un contacto
mi_contacto = Contacto(1, "Daniel", "Pérez", "García", "123456", "Universidad")

# acceder a las propiedades
print(f"id: {mi_contacto.id}")
print(f"Nombre: {mi_contacto.nombre}")
print(f"Apellido1: {mi_contacto.apellido1}")
print(f"Apellido2: {mi_contacto.apellido2}")
print(f"Tlf: {mi_contacto.telefono}")
print(f"Notas: {mi_contacto.notas}")

# cambio en propiedades
mi_contacto.notas = "Trabajo"
print(f"Nuevas Notas: {mi_contacto.notas}")


#-----------------------------------------------------------------------------------------
# ejemplo3
#       @classmethod
#       metodo de clase
#       transforma un método en un método de clase
#-----------------------------------------------------------------------------------------

class MiClase:
    contador_instancias = 0  
            # atributo de clase (variable de clase)
            # sin self delante y definida fuera de cualquier método

    def __init__(self, valor):
            # __init__ método constructor de la clase
            # se llama automáticamente cuando se crea una nueva instancia de una clase
            # su función principal es inicializar los atributos de la instancia
        MiClase.contador_instancias += 1

    @classmethod
    def obtener_contador_instancias(cls):
        return cls.contador_instancias

print("----Ejemplo3")

# instancias de la clase
objeto1 = MiClase(10)
objeto2 = MiClase(20)
objeto3 = MiClase(30)


contador = MiClase.obtener_contador_instancias()
        # contador no será un objeto
        # será un int
        # al llamar al método de clase para obtener el contador de instancias
print(f"Contador de instancias: {contador}")  # output: 3



#-----------------------------------------------------------------------------------------
# ejemplo4
#       decorador de clase
#-----------------------------------------------------------------------------------------

def decorador_clase(cls):
    cls.atributo = "Este es un nuevo atributo de la clase"
    return cls
        # cls es una convención utilizada para referirse a 
        # la clase en sí dentro de un decorador de clase

@decorador_clase
class MiClase:
    pass

print("----Ejemplo4")

objeto = MiClase()         # nuevo objeto del tipo clase
print(objeto.atributo)     # imprime atributo del objeto


    