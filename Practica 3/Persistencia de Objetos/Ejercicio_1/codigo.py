import json
import os
from typing import Optional

"""
1. Sea el siguiente diagrama de clases: 
a) Implementa el método guardarEmpleado(Empleado e) para almacenar 
empleados.
b) Implementa buscaEmpleado(String n) a traves del nombre, para ver los datos 
del Empleado n. 
c) Implementa mayorSalario(float sueldo), que devuelva al primer empleado con 
sueldo mayor al ingresado. 
"""
class Empleado:
    def __init__(self, nombre: str, edad: int, salario: float) -> None:
        self.__nombre = nombre
        self.__edad = edad
        self.__salario = salario

    def to_dict(self) -> dict:
        return {
            "nombre": self.__nombre,
            "edad": self.__edad,
            "salario": self.__salario
        }

    @staticmethod
    def from_dict(data: dict) -> "Empleado":
        return Empleado(
            data["nombre"],
            data["edad"],
            data["salario"]
        )

    def __str__(self) -> str:
        return f"Empleado(nombre={self.__nombre}, edad={self.__edad}, salario={self.__salario})"


class ArchivoEmpleado:
    def __init__(self, nomA: str) -> None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.__nomA = os.path.join(base_dir, nomA)

    def crearArchivo(self) -> None:
        if not os.path.exists(self.__nomA):
            carpeta = os.path.dirname(self.__nomA)
            if carpeta and not os.path.exists(carpeta):
                os.makedirs(carpeta, exist_ok=True)
            with open(self.__nomA, "w") as f:
                json.dump([], f)

    def guardarEmpleado(self, e: Empleado) -> None:
        if not os.path.exists(self.__nomA):
            self.crearArchivo()
        with open(self.__nomA, "r") as f:
            datos = json.load(f)
        datos.append(e.to_dict())
        with open(self.__nomA, "w") as f:
            json.dump(datos, f)

    def buscaEmpleado(self, n: str) -> Optional[Empleado]:
        if not os.path.exists(self.__nomA):
            return None
        with open(self.__nomA, "r") as f:
            datos = json.load(f)
        for item in datos:
            if item.get("nombre") == n:
                return Empleado.from_dict(item)
        return None

    def mayorSalario(self, sueldo: float) -> Optional[Empleado]:
        if not os.path.exists(self.__nomA):
            return None
        with open(self.__nomA, "r") as f:
            datos = json.load(f)
        for item in datos:
            if item.get("salario", 0) > sueldo:
                return Empleado.from_dict(item)
        return None

archivo = ArchivoEmpleado("empleados.json")
archivo.crearArchivo()
archivo.guardarEmpleado(Empleado("Ana", 30, 2000.0))
archivo.guardarEmpleado(Empleado("Luis", 25, 2500.0))
archivo.guardarEmpleado(Empleado("Carlos", 40, 1800.0))

print(archivo.buscaEmpleado("Luis"))      
print(archivo.mayorSalario(1900.0))        
