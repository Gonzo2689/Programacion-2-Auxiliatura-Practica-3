import json
import os
from typing import Optional

"""
3.- Sea el siguiente diagrama de clases: 
a) Implementar el diagrama de clases. 
b) Implementa buscarCliente(int c) a través del id. 
c) Implementa buscarCelularCliente(int c), que devuelva los datos del cliente 
junto al número de celular.
"""
class Cliente:
    def __init__(self, id: int, nombre: str, telefono: int) -> None:
        self.__id = id
        self.__nombre = nombre
        self.__telefono = telefono

    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "telefono": self.__telefono
        }

    @staticmethod
    def from_dict(data: dict) -> "Cliente":
        return Cliente(
            data["id"],
            data["nombre"],
            data["telefono"]
        )

    def __str__(self) -> str:
        return f"Cliente(id={self.__id}, nombre={self.__nombre}, telefono={self.__telefono})"


class ArchivoCliente:
    def __init__(self, nomA: str) -> None:          
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.__nomA = os.path.join(base_dir, nomA)

    def crearArchivo(self) -> None:
        carpeta = os.path.dirname(self.__nomA)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta, exist_ok=True)
        with open(self.__nomA, "w") as f:
            json.dump([], f)

    def guardarCliente(self, c: Cliente) -> None:
        if not os.path.exists(self.__nomA):
            self.crearArchivo()
        with open(self.__nomA, "r") as f:
            datos = json.load(f)
        datos.append(c.to_dict())
        with open(self.__nomA, "w") as f:
            json.dump(datos, f)

    def buscaCliente(self, id: int) -> Optional[Cliente]:
        if not os.path.exists(self.__nomA):
            return None
        with open(self.__nomA, "r") as f:
            datos = json.load(f)
        for item in datos:
            if item.get("id") == id:
                return Cliente.from_dict(item)
        return None

    def buscarCelularCliente(self, telefono: int) -> Optional[Cliente]:
        if not os.path.exists(self.__nomA):
            return None
        with open(self.__nomA, "r") as f:
            datos = json.load(f)
        for item in datos:
            if item.get("telefono") == telefono:
                return Cliente.from_dict(item)
        return None

archivo = ArchivoCliente("clientes.json")
archivo.crearArchivo()
archivo.guardarCliente(Cliente(1, "Juan", 123456789))
archivo.guardarCliente(Cliente(2, "Maria", 987654321))

print(archivo.buscaCliente(1))                 
print(archivo.buscarCelularCliente(987654321)) 
