package examen.veterinaria.model;

public class Mascota {
    private final String codigo;
    private final String nombre;
    private final Especie especie;
    private final int edad;
    private final String cedulaCliente;
    public Mascota(String codigo, String nombre, Especie especie, int edad, String cedulaCliente) {
        this.codigo = validar(codigo, "Código");
        this.nombre = validar(nombre, "Nombre");
        if (especie == null) throw new IllegalArgumentException("Seleccione una especie.");
        if (edad < 0 || edad > 40) throw new IllegalArgumentException("La edad debe estar entre 0 y 40 años.");
        this.especie = especie;
        this.edad = edad;
        this.cedulaCliente = validar(cedulaCliente, "Cédula del cliente");
    }
    private static String validar(String dato, String campo) {
        if (dato == null || dato.isBlank() || dato.contains(";") || dato.contains("\n") || dato.contains("\r"))
            throw new IllegalArgumentException(campo + " es obligatorio y no admite ; ni saltos de línea.");
        return dato.trim();
    }
    public String getCodigo() { return codigo; }
    public String getNombre() { return nombre; }
    public Especie getEspecie() { return especie; }
    public int getEdad() { return edad; }
    public String getCedulaCliente() { return cedulaCliente; }
    @Override public String toString() { return codigo + " | " + nombre + " | " + especie + " | " + edad + " años | Dueño: " + cedulaCliente; }
}
