package examen.veterinaria.repository;
import examen.veterinaria.model.Cliente;
import java.util.List;

public interface RepositorioCliente {
    List<Cliente> cargarTodos();
    void insertar(Cliente cliente);
}
