package examen.veterinaria;
import examen.veterinaria.controller.VeterinariaController;
import examen.veterinaria.repository.*;
import examen.veterinaria.service.VeterinariaService;
import examen.veterinaria.view.VentanaVeterinaria;
import javax.swing.SwingUtilities;

public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            RepositorioCliente clientes = new RepositorioClienteTxt("datos/clientes.txt");
            RepositorioMascota mascotas = new RepositorioMascotaTxt("datos/mascotas.txt", clientes);
            VeterinariaService service = new VeterinariaService(clientes,mascotas);
            new VentanaVeterinaria(new VeterinariaController(service)).setVisible(true);
        });
    }
}
