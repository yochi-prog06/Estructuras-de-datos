package examen.veterinaria.repository;
import examen.veterinaria.model.Mascota;
import java.util.List;

public interface RepositorioMascota {
    List<Mascota> cargarTodos();
    void insertar(Mascota mascota);
    void actualizar(Mascota mascota);
    void eliminar(String codigo);
    List<String> listarConDueno();
}
