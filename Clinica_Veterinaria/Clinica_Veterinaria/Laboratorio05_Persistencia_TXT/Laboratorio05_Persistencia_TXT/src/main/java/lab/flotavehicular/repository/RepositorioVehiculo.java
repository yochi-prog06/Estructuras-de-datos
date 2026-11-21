package lab.flotavehicular.repository;

import lab.flotavehicular.model.Vehiculo;

import java.util.List;

/**
 * Repository: define lo que la aplicación necesita de cualquier almacenamiento.
 */
public interface RepositorioVehiculo {

    List<Vehiculo> cargarTodos();

    void guardarTodos(List<Vehiculo> vehiculos);
}
