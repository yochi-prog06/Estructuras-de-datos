# Laboratorio 05 - versión con persistencia TXT

Esta versión parte del laboratorio de flota vehicular y agrega una separación más clara por capas.

## Cambios principales

- Los vehículos se recuperan y se guardan en `datos/vehiculos.txt`.
- `RepositorioVehiculo` define el contrato de persistencia.
- `RepositorioVehiculoTxt` implementa ese contrato con un archivo de texto.
- `FlotaService` mantiene la lista de trabajo y coordina el guardado.
- `DatosVehiculo` transporta la información del formulario.
- `VehiculoFactory` decide cuál subtipo de vehículo construir.
- El `pom.xml` usa `Main` como clase de entrada y conserva solo las dependencias utilizadas.

## Ejecución

1. Abrir la carpeta como proyecto Maven en IntelliJ IDEA.
2. Configurar un JDK compatible con las versiones indicadas en `pom.xml`.
3. Ejecutar la clase `lab.flotavehicular.Main`.
4. Registrar vehículos y cerrar la aplicación.
5. Revisar `datos/vehiculos.txt` y volver a abrir la aplicación para comprobar la persistencia.

## Formato del TXT

Cada vehículo ocupa una línea con campos separados por punto y coma:

```text
tipo;placa;marca;kilometraje;estado;energia;ciclos;tonelaje;carga;tipoCarga
```

La `List<Vehiculo>` sigue existiendo como memoria de trabajo. El TXT es el almacenamiento permanente entre ejecuciones.
