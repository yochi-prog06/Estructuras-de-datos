package examen.veterinaria.model;

public class Cliente {
    private final String cedula;
    private final String nombre;
    private final String telefono;
    public Cliente(String cedula, String nombre, String telefono) {
        this.cedula = validar(cedula, "Cédula");
        this.nombre = validar(nombre, "Nombre");
        this.telefono = validar(telefono, "Teléfono");
    }
    private static String validar(String valor, String campo) {
        if (valor == null || valor.isBlank() || valor.contains(";") || valor.contains("\n") || valor.contains("\r"))
            throw new IllegalArgumentException(campo + " es obligatorio y no puede contener ; ni saltos de línea.");
        return valor.trim();
    }
    public String getCedula() { return cedula; }
    public String getNombre() { return nombre; }
    public String getTelefono() { return telefono; }
    @Override public String toString() { return cedula + " | " + nombre + " | Tel: " + telefono; }
}
