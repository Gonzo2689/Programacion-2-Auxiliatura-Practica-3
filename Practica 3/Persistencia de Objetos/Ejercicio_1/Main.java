import java.io.*;
import java.util.*;

/* 1. Sea el siguiente diagrama de clases: 
a) Implementa el método guardarEmpleado(Empleado e) para almacenar 
empleados.
b) Implementa buscaEmpleado(String n) a traves del nombre, para ver los datos 
del Empleado n. 
c) Implementa mayorSalario(float sueldo), que devuelva al primer empleado con 
sueldo mayor al ingresado. */
public class Main {
    public static void main(String[] args) {
        ArchivoEmpleado archivo = new ArchivoEmpleado("empleados.txt");
        archivo.crearArchivo();
        archivo.guardarEmpleado(new Empleado("Ana", 30, 2000.0f));
        archivo.guardarEmpleado(new Empleado("Luis", 25, 2500.0f));
        archivo.guardarEmpleado(new Empleado("Carlos", 40, 1800.0f));

        System.out.println(archivo.buscaEmpleado("Luis"));
        System.out.println(archivo.mayorSalario(1900.0f));
    }
}

class Empleado {
    private String nombre;
    private int edad;
    private float salario;

    public Empleado(String nombre, int edad, float salario) {
        this.nombre = nombre;
        this.edad = edad;
        this.salario = salario;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    public float getSalario() {
        return salario;
    }

    @Override
    public String toString() {
        return "Empleado(nombre=" + nombre + ", edad=" + edad + ", salario=" + salario + ")";
    }
}

class ArchivoEmpleado {
    private final String ruta;

    public ArchivoEmpleado(String nombreArchivo) {
        this.ruta = new File(System.getProperty("user.dir"), nombreArchivo).getAbsolutePath();
    }

    public void crearArchivo() {
        File f = new File(ruta);
        try {
            File parent = f.getParentFile();
            if (parent != null && !parent.exists()) parent.mkdirs();
            if (!f.exists()) f.createNewFile();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void guardarEmpleado(Empleado e) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(ruta, true))) {
            bw.write(e.getNombre() + "," + e.getEdad() + "," + e.getSalario());
            bw.newLine();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public Empleado buscaEmpleado(String n) {
        try (BufferedReader br = new BufferedReader(new FileReader(ruta))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",");
                if (parts.length == 3 && parts[0].equals(n)) {
                    return new Empleado(parts[0], Integer.parseInt(parts[1]), Float.parseFloat(parts[2]));
                }
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return null;
    }

    public Empleado mayorSalario(float sueldo) {
        try (BufferedReader br = new BufferedReader(new FileReader(ruta))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",");
                float sal = Float.parseFloat(parts[2]);
                if (sal > sueldo) {
                    return new Empleado(parts[0], Integer.parseInt(parts[1]), sal);
                }
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return null;
    }
}
