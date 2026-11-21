package lab.flotavehicular.dto;

import lab.flotavehicular.model.TipoCarga;
import lab.flotavehicular.model.TipoVehiculo;

/**
 * DTO: transporta los datos capturados por la vista hacia la fábrica.
 * Los campos que no corresponden al tipo seleccionado se mantienen en cero o null.
 */
public record DatosVehiculo(
        String placa,
        String marca,
        int kilometraje,
        TipoVehiculo tipo,
        double nivelEnergia,
        double tonelajeMaximo,
        TipoCarga tipoCarga) {
}
