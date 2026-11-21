package examen.veterinaria.service;
import examen.veterinaria.model.*;
import examen.veterinaria.repository.*;
import java.util.*;

public class VeterinariaService {
    private final RepositorioCliente clientes;
    private final RepositorioMascota mascotas;
    public VeterinariaService(RepositorioCliente clientes, RepositorioMascota mascotas) {
        this.clientes = clientes; this.mascotas = mascotas;
    }
    public List<Cliente> listarClientes() { return clientes.cargarTodos(); }
    public List<Mascota> listarMascotas() { return mascotas.cargarTodos(); }
    public Cliente buscarCliente(String cedula) {
        if (cedula == null || cedula.isBlank()) throw new IllegalArgumentException("Indique la cédula.");
        for (Cliente c : clientes.cargarTodos()) if(c.getCedula().equalsIgnoreCase(cedula.trim())) return c;
        return null;
    }
    public void registrarCliente(String cedula, String nombre, String telefono) {
        Cliente c = new Cliente(cedula,nombre,telefono);
        if(buscarCliente(c.getCedula()) != null) throw new IllegalArgumentException("La cédula ya está registrada.");
        clientes.insertar(c);
    }
    private void verificarDueno(String cedula) {
        if(buscarCliente(cedula) == null) throw new IllegalArgumentException("Registre primero al cliente dueño de la mascota.");
    }
    public void registrarMascota(String codigo,String nombre,Especie especie,int edad,String cedulaCliente) {
        Mascota m = new Mascota(codigo,nombre,especie,edad,cedulaCliente);
        verificarDueno(m.getCedulaCliente());
        for (Mascota anterior: listarMascotas()) if(anterior.getCodigo().equalsIgnoreCase(m.getCodigo()))
            throw new IllegalArgumentException("El código de mascota ya existe.");
        mascotas.insertar(m);
    }
    public void actualizarMascota(String codigo,String nombre,Especie especie,int edad,String cedulaCliente) {
        Mascota m = new Mascota(codigo,nombre,especie,edad,cedulaCliente);
        verificarDueno(m.getCedulaCliente()); mascotas.actualizar(m);
    }
    public void eliminarMascota(String codigo) {
        if(codigo == null || codigo.isBlank()) throw new IllegalArgumentException("Indique el código.");
        mascotas.eliminar(codigo.trim());
    }
    public List<Mascota> mascotasPorCliente(String cedula) {
        if(cedula == null || cedula.isBlank()) throw new IllegalArgumentException("Indique la cédula para filtrar.");
        List<Mascota> resultado = new ArrayList<>();
        for (Mascota m : mascotas.cargarTodos()) if(m.getCedulaCliente().equalsIgnoreCase(cedula.trim())) resultado.add(m);
        return resultado;
    }
    public String listarMascotasConDueno() {
        List<String> filas = mascotas.listarConDueno();
        if(filas.isEmpty()) return "No hay mascotas registradas.";
        StringBuilder sb = new StringBuilder();
        for (String fila : filas) sb.append(fila).append('\n');
        return sb.toString();
    }
}
