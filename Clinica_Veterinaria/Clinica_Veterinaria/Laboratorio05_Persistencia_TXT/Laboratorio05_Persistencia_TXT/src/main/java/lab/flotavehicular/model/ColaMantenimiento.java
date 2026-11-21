package lab.flotavehicular.model;

import java.util.LinkedList;
import java.util.Queue;
import java.util.List;
import java.util.ArrayList;

// El <T extends Vehiculo> garantiza que esta cola es exclusivamente para vehículos
public class ColaMantenimiento<T extends Vehiculo> {

    // Usamos la interfaz Queue de Java Collections
    private Queue<T> filaDeEspera;

    public ColaMantenimiento() {
        // LinkedList implementa la interfaz Queue (FIFO - Primero en entrar, primero en salir)
        this.filaDeEspera = new LinkedList<>();
    }

    // Agregar a la cola
    public void encolar(T vehiculo) {

        if (vehiculo.getEstado() == EstadoVehiculo.TALLER) {
            throw new IllegalStateException(
                    "El vehículo ya se encuentra en mantenimiento."
            );
        }

        if (vehiculo.getEstado() == EstadoVehiculo.EN_RUTA) {
            throw new IllegalStateException(
                    "No puede enviar a mantenimiento un vehículo que está en ruta."
            );
        }

        vehiculo.setEstado(EstadoVehiculo.TALLER);
        filaDeEspera.offer(vehiculo);
    }

    // Reconstruye la cola al cargar vehículos que quedaron en TALLER en el TXT.
    public void restaurarPendiente(T vehiculo) {
        if (vehiculo.getEstado() == EstadoVehiculo.TALLER
                && !filaDeEspera.contains(vehiculo)) {
            filaDeEspera.offer(vehiculo);
        }
    }

    // Atender al primer vehículo
    public T atenderSiguiente() {
        if (filaDeEspera.isEmpty()) {
            throw new IllegalStateException(
                    "No hay vehículos en la cola de mantenimiento."
            );
        }

        T vehiculoAtendido = filaDeEspera.poll();
        vehiculoAtendido.setEstado(EstadoVehiculo.DISPONIBLE);

        return vehiculoAtendido;
    }

    // Métodos utilitarios para la vista gráfica
    public boolean estaVacia() {
        return filaDeEspera.isEmpty();
    }

    public int cantidadPendientes() {
        return filaDeEspera.size();
    }

    public List<T> obtenerListaPendientes() {
        return new ArrayList<>(filaDeEspera);
    }
}
