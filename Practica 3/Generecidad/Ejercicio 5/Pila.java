import java.util.ArrayList;
import java.util.List;
/* 5. Crea una clase genérica Pila<T> 
a) Implementa un método para apilar 
b) Implementa un método para des apilar 
c) Prueba la pila con diferentes tipos de datos 
d) Muestra los datos de la pila*/
public class Pila<T> {
    private List<T> elementos = new ArrayList<>();

    public void apilar(T elemento) {
        elementos.add(elemento);
    }

    public T desapilar() {
        if (elementos.isEmpty()) {
            return null;
        }
        return elementos.remove(elementos.size() - 1);
    }

    @Override
    public String toString() {
        return "Pila" + elementos;
    }

    public static void main(String[] args) {
        Pila<Integer> pilaEnteros = new Pila<>();
        pilaEnteros.apilar(1);
        pilaEnteros.apilar(2);
        pilaEnteros.apilar(3);
        System.out.println(pilaEnteros);
        System.out.println(pilaEnteros.desapilar());
        System.out.println(pilaEnteros);

        Pila<String> pilaCadenas = new Pila<>();
        pilaCadenas.apilar("hola");
        pilaCadenas.apilar("mundo");
        System.out.println(pilaCadenas);
        System.out.println(pilaCadenas.desapilar());
        System.out.println(pilaCadenas);

        Pila<Double> pilaFlotantes = new Pila<>();
        pilaFlotantes.apilar(1.5);
        pilaFlotantes.apilar(2.5);
        System.out.println(pilaFlotantes);
        System.out.println(pilaFlotantes.desapilar());
        System.out.println(pilaFlotantes);
    }
}
