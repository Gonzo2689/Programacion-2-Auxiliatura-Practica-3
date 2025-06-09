from typing import TypeVar, Generic, List, Optional, Any
"""
5. Crea una clase genérica Pila<T> 
a) Implementa un método para apilar 
b) Implementa un método para des apilar 
c) Prueba la pila con diferentes tipos de datos 
d) Muestra los datos de la pila
"""
T = TypeVar('T')

class Pila(Generic[T]):
    def __init__(self) -> None:
        self.__elementos: List[T] = []

    def apilar(self, elemento: T) -> None:
        self.__elementos.append(elemento)

    def desapilar(self) -> Optional[T]:
        if self.__elementos:
            return self.__elementos.pop()
        return None

    def __str__(self) -> str:
        return f"Pila({self.__elementos})"

pila_enteros = Pila[int]()
pila_enteros.apilar(1)
pila_enteros.apilar(2)
pila_enteros.apilar(3)
print(pila_enteros)
print(pila_enteros.desapilar())
print(pila_enteros)

pila_cadenas = Pila[str]()
pila_cadenas.apilar("hola")
pila_cadenas.apilar("mundo")
print(pila_cadenas)
print(pila_cadenas.desapilar())
print(pila_cadenas)

pila_flotantes = Pila[float]()
pila_flotantes.apilar(1.5)
pila_flotantes.apilar(2.5)
print(pila_flotantes)
print(pila_flotantes.desapilar())
print(pila_flotantes)
