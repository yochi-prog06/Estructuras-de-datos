package examen.veterinaria.repository;

import examen.veterinaria.model.*;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;

public class RepositorioMascotaTxt implements RepositorioMascota {
    private final Path archivo;
    private final RepositorioCliente clientes;
    public RepositorioMascotaTxt(String ruta, RepositorioCliente clientes) { archivo = Path.of(ruta); this.clientes = clientes; }
    @Override public List<Mascota> cargarTodos() {
        List<Mascota> lista = new ArrayList<>();
        if (!Files.exists(archivo)) return lista;
        try {
            for (String linea : Files.readAllLines(archivo, StandardCharsets.UTF_8)) {
                if (linea.isBlank()) continue;
                String[] c = linea.split(";", -1);
                if (c.length != 5) throw new IllegalArgumentException("Línea de mascota inválida.");
                lista.add(new Mascota(c[0], c[1], Especie.valueOf(c[2]), Integer.parseInt(c[3]), c[4]));
            }
            return lista;
        } catch (IOException e) { throw new PersistenciaException("No se pudieron cargar las mascotas del TXT.", e); }
    }
    @Override public List<String> listarConDueno() {
        List<String> filas = new ArrayList<>();
        for (Mascota m : cargarTodos()) {
            String dueno = "NO ENCONTRADO";
            for (examen.veterinaria.model.Cliente c : clientes.cargarTodos()) {
                if(c.getCedula().equalsIgnoreCase(m.getCedulaCliente())) { dueno = c.getNombre(); break; }
            }
            filas.add(m + " | Cliente: " + dueno);
        }
        return filas;
    }
    @Override public void insertar(Mascota mascota) {
        List<Mascota> datos = cargarTodos();
        for (Mascota m : datos) if (m.getCodigo().equalsIgnoreCase(mascota.getCodigo()))
            throw new IllegalArgumentException("Ya existe ese código de mascota.");
        datos.add(mascota); guardar(datos);
    }
    @Override public void actualizar(Mascota mascota) {
        List<Mascota> datos = cargarTodos();
        for (int i=0; i<datos.size(); i++) {
            if (datos.get(i).getCodigo().equalsIgnoreCase(mascota.getCodigo())) {
                datos.set(i, mascota); guardar(datos); return;
            }
        }
        throw new IllegalArgumentException("No existe la mascota que desea actualizar.");
    }
    @Override public void eliminar(String codigo) {
        List<Mascota> datos = cargarTodos();
        boolean eliminado = datos.removeIf(m -> m.getCodigo().equalsIgnoreCase(codigo.trim()));
        if (!eliminado) throw new IllegalArgumentException("No existe la mascota que desea eliminar.");
        guardar(datos);
    }
    private void guardar(List<Mascota> datos) {
        List<String> lineas = new ArrayList<>();
        for (Mascota m : datos) lineas.add(m.getCodigo()+";"+m.getNombre()+";"+m.getEspecie()+";"+m.getEdad()+";"+m.getCedulaCliente());
        try {
            if (archivo.getParent()!=null) Files.createDirectories(archivo.getParent());
            Files.write(archivo, lineas, StandardCharsets.UTF_8);
        } catch (IOException e) { throw new PersistenciaException("No se pudieron guardar las mascotas.", e); }
    }
}
