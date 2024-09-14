import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox

class PersonalInfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle('Formulario de Información Personal')
        self.setGeometry(100, 100, 400, 200)

        # Layout principal
        layout = QVBoxLayout()

        # Etiqueta y campo de entrada para el número de cédula
        self.cedula_label = QLabel('Número de DUI:')
        layout.addWidget(self.cedula_label)

        self.cedula_input = QLineEdit()
        layout.addWidget(self.cedula_input)

        # Etiqueta y campo de entrada para el nombre completo
        self.nombre_label = QLabel('Nombre Completo:')
        layout.addWidget(self.nombre_label)

        self.nombre_input = QLineEdit()
        layout.addWidget(self.nombre_input)

        # Botón para enviar la información
        self.submit_button = QPushButton('Enviar')
        self.submit_button.clicked.connect(self.submit_info)
        layout.addWidget(self.submit_button)

        # Configurar layout
        self.setLayout(layout)

    def submit_info(self):
        # Obtener los datos ingresados
        cedula = self.cedula_input.text()
        nombre = self.nombre_input.text()

        # Validar que se hayan ingresado todos los datos
        if not cedula or not nombre:
            QMessageBox.warning(self, 'Error', 'Por favor, ingrese tanto el número de cédula como el nombre completo.')
        else:
            QMessageBox.information(self, 'Información Enviada', f'Número de Cédula: {cedula}\nNombre Completo: {nombre}')

# Inicializar la aplicación directamebnte 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PersonalInfoWindow()
    window.show()
    sys.exit(app.exec_())
