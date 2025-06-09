from typing import TypeVar, Generic
"""1. Crea una clase genérica Caja<T> para guardar algún tipo de objeto 
a) Agrega métodos guardar() y obtener() 
b) Crea dos instancias de la caja y almacena 2 datos de diferente tipo 
c) Muestra el contenido de las cajas """
T=TypeVar('T')
class Caja(Generic[T]):
    def __init__(self):
        self.__contenido: T=None
    def guardar(self, objeto: T):
        self.__contenido = objeto
    def obtener(self) ->T:
        return self.__contenido

caja_int = Caja[int]()
caja_int.guardar(22)
caja_str = Caja[str]()
caja_str.guardar("HOLA MUNDO")

print(f"contenido de la caja_int: {caja_int.obtener()}") 
print(f"contenido de la caja_str: {caja_str.obtener()}")     
        