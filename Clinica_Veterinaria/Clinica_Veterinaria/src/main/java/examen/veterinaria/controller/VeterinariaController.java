package examen.veterinaria.controller;
import examen.veterinaria.model.*;
import examen.veterinaria.service.VeterinariaService;
import java.util.List;

public class VeterinariaController {
    private final VeterinariaService servicio;
    public VeterinariaController(VeterinariaService servicio) { this.servicio = servicio; }
    public void registrarCliente(String cedula,String nombre,String telefono) { servicio.registrarCliente(cedula,nombre,telefono); }
    public void registrarMascota(String codigo,String nombre,Especie especie,String edad,String cedula) { servicio.registrarMascota(codigo,nombre,especie,Integer.parseInt(edad.trim()),cedula); }
    public void actualizarMascota(String codigo,String nombre,Especie especie,String edad,String cedula) { servicio.actualizarMascota(codigo,nombre,especie,Integer.parseInt(edad.trim()),cedula); }
    public void eliminarMascota(String codigo) { servicio.eliminarMascota(codigo); }
    public String verClientes() {
        List<Cliente> datos = servicio.listarClientes();
        if(datos.isEmpty()) return "No hay clientes registrados.";
        StringBuilder sb = new StringBuilder();
        for(Cliente c : datos) sb.append(c).append('\n');
        return sb.toString();
    }
    public String verMascotas() { return servicio.listarMascotasConDueno(); }
    public String buscarPorCliente(String cedula) {
        List<Mascota> datos = servicio.mascotasPorCliente(cedula);
        if(datos.isEmpty()) return "No hay mascotas para esa cédula.";
        StringBuilder sb = new StringBuilder();
        for(Mascota m : datos) sb.append(m).append('\n');
        return sb.toString();
    }
}
