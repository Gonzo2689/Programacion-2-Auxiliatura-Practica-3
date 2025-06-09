from typing import TypeVar, Generic, List, Optional, Any

T = TypeVar('T')

class Catalogo(Generic[T]):
    def __init__(self) -> None:
        self.__elementos: List[T] = []

    def agregar(self, elemento: T) -> None:
        self.__elementos.append(elemento)

    def buscar(self, valor: Any) -> Optional[T]:
        for item in self.__elementos:
            for atributo in vars(item).values():
                if atributo == valor:
                    return item
        return None

class Libro:
    def __init__(self, id: int, titulo: str, autor: str) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor

    def __str__(self) -> str:
        return f"Libro #{self.__id}: '{self.__titulo}' de {self.__autor}"

class Producto:
    def __init__(self, id: int, nombre: str, precio: float) -> None:
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio

    def __str__(self) -> str:
        return f"Producto #{self.__id}: {self.__nombre} (Bs. {self.__precio})"

catalogo_libros = Catalogo[Libro]()
catalogo_libros.agregar(Libro(1, "1984", "George Orwell"))
catalogo_libros.agregar(Libro(2, "El Principito", "Antoine de Saint-Exupéry"))

print(catalogo_libros.buscar("1984"))
print(catalogo_libros.buscar("Asimov"))

catalogo_productos = Catalogo[Producto]()
catalogo_productos.agregar(Producto(1, "Laptop", 15000.0))
catalogo_productos.agregar(Producto(2, "Smartphone", 800.0))

print(catalogo_productos.buscar("Laptop"))
print(catalogo_productos.buscar("Tablet"))
