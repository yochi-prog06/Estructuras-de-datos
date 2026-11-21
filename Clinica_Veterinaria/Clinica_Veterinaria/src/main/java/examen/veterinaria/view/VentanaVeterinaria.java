package examen.veterinaria.view;

import examen.veterinaria.controller.VeterinariaController;
import examen.veterinaria.model.Especie;
import javax.swing.*;
import java.awt.*;

public class VentanaVeterinaria extends JFrame {
    private final VeterinariaController controller;
    private final JTextField txtCedula=new JTextField(12), txtNombreCliente=new JTextField(16), txtTelefono=new JTextField(12);
    private final JTextField txtCodigo=new JTextField(8), txtNombreMascota=new JTextField(12), txtEdad=new JTextField(5), txtDueno=new JTextField(12), txtFiltro=new JTextField(12);
    private final JComboBox<Especie> cmbEspecie=new JComboBox<>(Especie.values());
    private final JTextArea salida=new JTextArea(16,64);
    private final JLabel estado=new JLabel("Sistema listo");
    public VentanaVeterinaria(VeterinariaController controller) {
        super("Clínica Veterinaria");
        this.controller=controller;
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(940,620); setLocationRelativeTo(null);
        setLayout(new BorderLayout(10,10));
        JTabbedPane pestañas=new JTabbedPane();
        pestañas.addTab("Clientes", panelClientes()); pestañas.addTab("Mascotas", panelMascotas());
        add(pestañas,BorderLayout.NORTH);
        JPanel centro=new JPanel(new BorderLayout(5,5));
        salida.setEditable(false); salida.setFont(new Font(Font.MONOSPACED,Font.PLAIN,12));
        centro.add(new JLabel("Resultados:"),BorderLayout.NORTH);
        centro.add(new JScrollPane(salida),BorderLayout.CENTER);
        add(centro,BorderLayout.CENTER);
        JPanel pie=new JPanel(new BorderLayout()); pie.add(estado,BorderLayout.CENTER);
        add(pie,BorderLayout.SOUTH);
        ejecutar(()->salida.setText(controller.verMascotas()));
    }
    private JPanel panelClientes() {
        JPanel p=new JPanel(new FlowLayout(FlowLayout.LEFT,8,9));
        p.add(new JLabel("Cédula:"));p.add(txtCedula);
        p.add(new JLabel("Nombre:"));p.add(txtNombreCliente);
        p.add(new JLabel("Teléfono:"));p.add(txtTelefono);
        JButton registrar=new JButton("Registrar cliente"), listar=new JButton("Listar clientes");
        p.add(registrar);p.add(listar);
        registrar.addActionListener(e->ejecutar(()->{controller.registrarCliente(txtCedula.getText(),txtNombreCliente.getText(),txtTelefono.getText());salida.setText(controller.verClientes());estado.setText("Cliente guardado.");}));
        listar.addActionListener(e->ejecutar(()->salida.setText(controller.verClientes())));
        return p;
    }
    private JPanel panelMascotas() {
        JPanel contenedor=new JPanel(new BorderLayout());
        JPanel datos=new JPanel(new FlowLayout(FlowLayout.LEFT,6,7));
        datos.add(new JLabel("Código:"));datos.add(txtCodigo);datos.add(new JLabel("Nombre:"));datos.add(txtNombreMascota);
        datos.add(new JLabel("Especie:"));datos.add(cmbEspecie);datos.add(new JLabel("Edad:"));datos.add(txtEdad);
        datos.add(new JLabel("Cédula dueño:"));datos.add(txtDueno);
        contenedor.add(datos,BorderLayout.NORTH);
        JPanel botones=new JPanel(new FlowLayout(FlowLayout.LEFT,8,6));
        JButton registrar=new JButton("Registrar mascota"), actualizar=new JButton("Actualizar mascota"), eliminar=new JButton("Eliminar mascota"), listar=new JButton("Listar con dueño"), filtrar=new JButton("Filtrar por cédula");
        botones.add(registrar);botones.add(actualizar);botones.add(eliminar);botones.add(listar);
        botones.add(new JLabel("Cédula:"));botones.add(txtFiltro);botones.add(filtrar);
        contenedor.add(botones,BorderLayout.SOUTH);
        registrar.addActionListener(e->ejecutar(()->{controller.registrarMascota(txtCodigo.getText(),txtNombreMascota.getText(),(Especie)cmbEspecie.getSelectedItem(),txtEdad.getText(),txtDueno.getText());salida.setText(controller.verMascotas());estado.setText("Mascota registrada.");}));
        actualizar.addActionListener(e->ejecutar(()->{controller.actualizarMascota(txtCodigo.getText(),txtNombreMascota.getText(),(Especie)cmbEspecie.getSelectedItem(),txtEdad.getText(),txtDueno.getText());salida.setText(controller.verMascotas());estado.setText("Mascota actualizada.");}));
        eliminar.addActionListener(e->ejecutar(()->{controller.eliminarMascota(txtCodigo.getText());salida.setText(controller.verMascotas());estado.setText("Mascota eliminada.");}));
        listar.addActionListener(e->ejecutar(()->salida.setText(controller.verMascotas())));
        filtrar.addActionListener(e->ejecutar(()->salida.setText(controller.buscarPorCliente(txtFiltro.getText()))));
        txtFiltro.addActionListener(e->filtrar.doClick());
        return contenedor;
    }
    private void ejecutar(Runnable tarea) {
        try { tarea.run(); }
        catch (RuntimeException e) { estado.setText("Error: "+e.getMessage()); JOptionPane.showMessageDialog(this,e.getMessage(),"Operación no realizada",JOptionPane.WARNING_MESSAGE); }
    }
}
