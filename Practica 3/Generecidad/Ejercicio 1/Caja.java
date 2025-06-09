 /*1. Crea una clase genérica Caja<T> para guardar algún tipo de objeto 
a) Agrega métodos guardar() y obtener() 
b) Crea dos instancias de la caja y almacena 2 datos de diferente tipo 
c) Muestra el contenido de las cajas*/
public class Caja<T> {
    private T contenido;

    public void guardar(T objeto) {
        this.contenido = objeto;
    }

    public T obtener() {
        return this.contenido;
    }

    public static void main(String[] args) {
        Caja<Integer> cajaInt = new Caja<>();
        cajaInt.guardar(22);

        Caja<String> cajaStr = new Caja<>();
        cajaStr.guardar("HOLA MUNDO");

        System.out.println("contenido de la caja_int: " + cajaInt.obtener());
        System.out.println("contenido de la caja_str: " + cajaStr.obtener());
    }
}
