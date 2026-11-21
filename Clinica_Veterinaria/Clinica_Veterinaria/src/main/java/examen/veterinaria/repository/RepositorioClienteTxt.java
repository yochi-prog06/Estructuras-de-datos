package examen.veterinaria.repository;

import examen.veterinaria.model.Cliente;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;

public class RepositorioClienteTxt implements RepositorioCliente {
    private final Path archivo;
    public RepositorioClienteTxt(String ruta) { archivo = Path.of(ruta); }
    @Override public List<Cliente> cargarTodos() {
        List<Cliente> lista = new ArrayList<>();
        if (!Files.exists(archivo)) return lista;
        try {
            for (String linea : Files.readAllLines(archivo, StandardCharsets.UTF_8)) {
                if (linea.isBlank()) continue;
                String[] c = linea.split(";", -1);
                if (c.length != 3) throw new IllegalArgumentException("Línea de cliente inválida.");
                lista.add(new Cliente(c[0], c[1], c[2]));
            }
            return lista;
        } catch (IOException e) { throw new PersistenciaException("No se pudieron cargar los clientes del TXT.", e); }
    }
    @Override public void insertar(Cliente cliente) {
        List<Cliente> datos = cargarTodos();
        for (Cliente existente : datos) if (existente.getCedula().equalsIgnoreCase(cliente.getCedula()))
            throw new IllegalArgumentException("Ya existe un cliente con esa cédula.");
        datos.add(cliente);
        guardar(datos);
    }
    private void guardar(List<Cliente> clientes) {
        List<String> lineas = new ArrayList<>();
        for (Cliente c : clientes) lineas.add(c.getCedula()+";"+c.getNombre()+";"+c.getTelefono());
        try {
            if (archivo.getParent()!=null) Files.createDirectories(archivo.getParent());
            Files.write(archivo, lineas, StandardCharsets.UTF_8);
        } catch (IOException e) { throw new PersistenciaException("No se pudieron guardar los clientes.", e); }
    }
}
