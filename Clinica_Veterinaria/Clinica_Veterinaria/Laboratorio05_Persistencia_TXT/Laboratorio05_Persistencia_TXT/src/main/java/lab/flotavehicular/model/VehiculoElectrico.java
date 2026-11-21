package lab.flotavehicular.model;

public class VehiculoElectrico extends Vehiculo {

    private double porcentajeBateria; // De 0.0 a 100.0
    private int ciclosDeCarga;        // Cuántas veces se ha cargado

    // Constructor completo
    public VehiculoElectrico(String placa, String marca, int kilometraje, double porcentajeBateria, int ciclosDeCarga) {
        super(placa, marca, kilometraje); // Envia placa, marca y km al padre (Vehiculo)
        this.porcentajeBateria = porcentajeBateria;
        this.ciclosDeCarga = ciclosDeCarga;
    }

    // Getter que la vista (el controlador) va a necesitar para la barra de progreso
    public double getPorcentajeBateria() {
        return porcentajeBateria;
    }

    public int getCiclosDeCarga() {
        return ciclosDeCarga;
    }

    // ==========================================
    // IMPLEMENTACIÓN DE LOS MÉTODOS OBLIGATORIOS
    // ==========================================

    @Override
    public void iniciarRuta() {
        // 1. Usamos una excepción estándar de Java, sin crear clases extra
        if (estado == EstadoVehiculo.EN_RUTA) {
            throw new IllegalStateException(
                    "El vehículo [" + placa + "] ya se encuentra en ruta."
            );
        }

        if (this.estado == EstadoVehiculo.TALLER) {
            throw new IllegalStateException("El vehículo [" + placa + "] está en el taller. No puede salir.");
        }

        if (this.porcentajeBateria < 15.0) {
            throw new IllegalStateException("Batería insuficiente (" + porcentajeBateria + "%). Conecte al cargador.");
        }

        // 2. Lógica específica del vehículo eléctrico al moverse
        this.porcentajeBateria -= 15.0; // Consume un 15% de batería por viaje
        this.kilometraje += 50;         // Simula que recorrió 50km
        this.estado = EstadoVehiculo.EN_RUTA;
    }

    @Override
    public TipoVehiculo getTipo() {
        return TipoVehiculo.ELECTRICO;
    }

    @Override
    public String evaluarEstadoGeneral() {
        // Lógica específica para carros eléctricos evaluando el estado de su batería
        if (ciclosDeCarga > 1000) {
            return "Alerta: Batería muy degradada, requiere reemplazo";
        } else if (porcentajeBateria < 20) {
            return "Requiere conexión a estación de carga";
        } else {
            return "Batería y sistemas óptimos";
        }
    }
}
