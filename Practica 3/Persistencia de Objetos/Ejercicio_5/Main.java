import java.io.*;
import java.util.*;
import java.util.AbstractMap.SimpleEntry;

public class Main {
    public static void main(String[] args) {
        ArchFarmacia archivo = new ArchFarmacia("farmacias.txt");
        archivo.crearArchivo();

        Farmacia f1 = new Farmacia("Farmacia Central", 1, "Av. Siempre Viva 742");
        f1.adicionarMedicamento(new Medicamento("Golpex", 101, "lastimaduras", 5.0));
        f1.adicionarMedicamento(new Medicamento("Resfriol", 102, "resfrio", 3.0));
        archivo.adicionar(f1);

        Farmacia f2 = new Farmacia("Farmacia Norte", 2, "Calle Falsa 123");
        f2.adicionarMedicamento(new Medicamento("TosLin", 201, "tos", 4.5));
        archivo.adicionar(f2);

        List<Farmacia> todas = archivo.listar();
        for (Farmacia f : todas) {
            System.out.println(f);
        }

        List<Medicamento> tos = archivo.mostrarMedicamentosTos(2);
        for (Medicamento m : tos) {
            System.out.println(m);
        }

        SimpleEntry<Integer,String> res = archivo.buscarSucursalConMedicamento("Golpex");
        if (res != null) {
            System.out.println("Sucursal: " + res.getKey() + ", Dirección: " + res.getValue());
        }
    }
}

class Medicamento {
    private String nombre;
    private int codMedicamento;
    private String tipo;
    private double precio;

    public Medicamento(String nombre, int codMedicamento, String tipo, double precio) {
        this.nombre = nombre;
        this.codMedicamento = codMedicamento;
        this.tipo = tipo;
        this.precio = precio;
    }

    public String getTipo() {
        return tipo;
    }

    public String toText() {
        return nombre + "," + codMedicamento + "," + tipo + "," + precio;
    }

    public static Medicamento fromText(String txt) {
        String[] p = txt.split(",", 4);
        return new Medicamento(
            p[0],
            Integer.parseInt(p[1]),
            p[2],
            Double.parseDouble(p[3])
        );
    }

    @Override
    public String toString() {
        return nombre + " (código " + codMedicamento + ", tipo " + tipo + ", precio " + precio + ")";
    }
}

class Farmacia {
    private String nombreFarmacia;
    private int sucursal;
    private String direccion;
    private List<Medicamento> medicamentos = new ArrayList<>();

    public Farmacia(String nombreFarmacia, int sucursal, String direccion) {
        this.nombreFarmacia = nombreFarmacia;
        this.sucursal = sucursal;
        this.direccion = direccion;
    }

    public void adicionarMedicamento(Medicamento m) {
        medicamentos.add(m);
    }

    public int getSucursal() {
        return sucursal;
    }

    public String getDireccion() {
        return direccion;
    }

    public List<Medicamento> mostrarMedicamentos(String tipo) {
        List<Medicamento> res = new ArrayList<>();
        for (Medicamento m : medicamentos) {
            if (m.getTipo().equals(tipo)) {
                res.add(m);
            }
        }
        return res;
    }

    public Medicamento buscaMedicamento(String nombre) {
        for (Medicamento m : medicamentos) {
            if (m.toString().startsWith(nombre + " ")) {
                return m;
            }
        }
        return null;
    }

    public String toText() {
        StringBuilder sb = new StringBuilder();
        sb.append(nombreFarmacia).append("|")
          .append(sucursal).append("|")
          .append(direccion).append("|");
        for (int i = 0; i < medicamentos.size(); i++) {
            if (i > 0) sb.append(";");
            sb.append(medicamentos.get(i).toText());
        }
        return sb.toString();
    }

    public static Farmacia fromText(String txt) {
        String[] parts = txt.split("\\|", 4);
        Farmacia f = new Farmacia(parts[0], Integer.parseInt(parts[1]), parts[2]);
        if (parts.length == 4 && !parts[3].isEmpty()) {
            String[] meds = parts[3].split(";");
            for (String mtxt : meds) {
                f.adicionarMedicamento(Medicamento.fromText(mtxt));
            }
        }
        return f;
    }

    @Override
    public String toString() {
        return nombreFarmacia + " (sucursal " + sucursal + ", " + direccion + ")";
    }
}

class ArchFarmacia {
    private String ruta;

    public ArchFarmacia(String nombreArchivo) {
        String base = System.getProperty("user.dir");
        this.ruta = base + File.separator + nombreArchivo;
    }

    public void crearArchivo() {
        try {
            File f = new File(ruta);
            File dir = f.getParentFile();
            if (dir != null && !dir.exists()) dir.mkdirs();
            if (!f.exists()) f.createNewFile();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void adicionar(Farmacia farm) {
        crearArchivo();
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(ruta, true))) {
            bw.write(farm.toText());
            bw.newLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public List<Farmacia> listar() {
        List<Farmacia> res = new ArrayList<>();
        File f = new File(ruta);
        if (!f.exists()) return res;
        try (BufferedReader br = new BufferedReader(new FileReader(ruta))) {
            String line;
            while ((line = br.readLine()) != null) {
                res.add(Farmacia.fromText(line));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return res;
    }

    public List<Medicamento> mostrarMedicamentosTos(int sucursal) {
        List<Medicamento> salida = new ArrayList<>();
        for (Farmacia f : listar()) {
            if (f.getSucursal() == sucursal) {
                salida.addAll(f.mostrarMedicamentos("tos"));
            }
        }
        return salida;
    }

    public SimpleEntry<Integer, String> buscarSucursalConMedicamento(String nombre) {
        for (Farmacia f : listar()) {
            if (f.buscaMedicamento(nombre) != null) {
                return new SimpleEntry<>(f.getSucursal(), f.getDireccion());
            }
        }
        return null;
    }
}
 