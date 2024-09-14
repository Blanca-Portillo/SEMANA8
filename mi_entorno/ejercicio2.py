import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox

class SecretKeyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle('Entrada de Clave Secreta')
        self.setGeometry(100, 100, 300, 150)

        # Layout principal
        layout = QVBoxLayout()

        # Etiqueta para pedir la clave secreta
        self.instruction_label = QLabel('Ingrese su clave secreta:')
        layout.addWidget(self.instruction_label)

        # Campo de entrada de texto para la clave secreta
        self.secret_key_input = QLineEdit()
        self.secret_key_input.setEchoMode(QLineEdit.Password)  # Modo de contraseña para ocultar caracteres
        layout.addWidget(self.secret_key_input)

        # Botón para enviar la clave
        self.submit_button = QPushButton('Enviar')
        self.submit_button.clicked.connect(self.submit_secret_key)
        layout.addWidget(self.submit_button)

        # Configurar layout
        self.setLayout(layout)

    def submit_secret_key(self):
        # Obtener la clave ingresada
        secret_key = self.secret_key_input.text()

        # Validar que se haya ingresado una clave
        if not secret_key:
            QMessageBox.warning(self, 'Error', 'Por favor, ingrese una clave secreta.')
        else:
            QMessageBox.information(self, 'Clave Secreta', f'La clave ingresada es: {secret_key}')

# Inicializar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SecretKeyWindow()
    window.show()
    sys.exit(app.exec_())
