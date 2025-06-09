import json
import os
from typing import List, Optional, Tuple

"""
5.- Sea el siguiente diagrama de clases:  
a) Crear, leer y mostrar un Archivo de Farmacias  
b) Mostrar los medicamentos para la tos, de la Sucursal numero X  
c) Mostrar el número de sucursal y su dirección que tienen el medicamento 
“Golpex”
"""
class Medicamento:
    def __init__(self, nombre: str, codMedicamento: int, tipo: str, precio: float) -> None:
        self.__nombre = nombre
        self.__codMedicamento = codMedicamento
        self.__tipo = tipo
        self.__precio = precio

    def to_dict(self) -> dict:
        return {
            "nombre": self.__nombre,
            "codMedicamento": self.__codMedicamento,
            "tipo": self.__tipo,
            "precio": self.__precio
        }

    @staticmethod
    def from_dict(data: dict) -> "Medicamento":
        return Medicamento(
            data["nombre"],
            data["codMedicamento"],
            data["tipo"],
            data["precio"]
        )

    def getTipo(self) -> str:
        return self.__tipo

    def __str__(self) -> str:
        return f"{self.__nombre} (código {self.__codMedicamento}, tipo {self.__tipo}, precio {self.__precio})"


class Farmacia:
    def __init__(self, nombreFarmacia: str, sucursal: int, direccion: str) -> None:
        self.__nombreFarmacia = nombreFarmacia
        self.__sucursal = sucursal
        self.__direccion = direccion
        self.__medicamentos: List[Medicamento] = []

    def to_dict(self) -> dict:
        return {
            "nombreFarmacia": self.__nombreFarmacia,
            "sucursal": self.__sucursal,
            "direccion": self.__direccion,
            "medicamentos": [m.to_dict() for m in self.__medicamentos]
        }

    @staticmethod
    def from_dict(data: dict) -> "Farmacia":
        f = Farmacia(data["nombreFarmacia"], data["sucursal"], data["direccion"])
        for m in data.get("medicamentos", []):
            f.__medicamentos.append(Medicamento.from_dict(m))
        return f

    def adicionarMedicamento(self, m: Medicamento) -> None:
        self.__medicamentos.append(m)

    def getSucursal(self) -> int:
        return self.__sucursal

    def getDireccion(self) -> str:
        return self.__direccion

    def mostrarMedicamentos(self, tipo: str) -> List[Medicamento]:
        return [m for m in self.__medicamentos if m.getTipo() == tipo]

    def buscaMedicamento(self, nombre: str) -> Optional[Medicamento]:
        for m in self.__medicamentos:
            if m._Medicamento__nombre == nombre:
                return m
        return None

    def __str__(self) -> str:
        return f"{self.__nombreFarmacia} (sucursal {self.__sucursal}, {self.__direccion})"


class ArchFarmacia:
    def __init__(self, na: str) -> None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.__ruta = os.path.join(base_dir, na)

    def crearArchivo(self) -> None:
        if not os.path.exists(self.__ruta):
            with open(self.__ruta, "w") as f:
                json.dump([], f)

    def adicionar(self, f: Farmacia) -> None:
        self.crearArchivo()
        with open(self.__ruta, "r") as jf:
            datos = json.load(jf)
        datos.append(f.to_dict())
        with open(self.__ruta, "w") as jf:
            json.dump(datos, jf)

    def listar(self) -> List[Farmacia]:
        if not os.path.exists(self.__ruta):
            return []
        with open(self.__ruta, "r") as jf:
            datos = json.load(jf)
        return [Farmacia.from_dict(item) for item in datos]

    def mostrarMedicamentosTos(self, sucursal: int) -> List[Medicamento]:
        resultado: List[Medicamento] = []
        for f in self.listar():
            if f.getSucursal() == sucursal:
                resultado.extend(f.mostrarMedicamentos("tos"))
        return resultado

    def buscarSucursalConMedicamento(self, nombre: str) -> Optional[Tuple[int, str]]:
        for f in self.listar():
            if f.buscaMedicamento(nombre):
                return (f.getSucursal(), f.getDireccion())
        return None

archivo = ArchFarmacia("farmacias.json")
archivo.crearArchivo()

f1 = Farmacia("Farmacia Central", 1, "Av. Siempre Viva 742")
f1.adicionarMedicamento(Medicamento("Golpex", 101, "lastimaduras", 5.0))
f1.adicionarMedicamento(Medicamento("Resfriol", 102, "resfrio", 3.0))
archivo.adicionar(f1)

f2 = Farmacia("Farmacia Norte", 2, "Calle Falsa 123")
f2.adicionarMedicamento(Medicamento("TosLin", 201, "tos", 4.5))
archivo.adicionar(f2)

print([str(f) for f in archivo.listar()])

print([str(m) for m in archivo.mostrarMedicamentosTos(2)])

print(archivo.buscarSucursalConMedicamento("Golpex"))
