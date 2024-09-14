import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class PersonalInfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle('Información Personal')
        self.setGeometry(100, 100, 400, 200)

        # Layout principal
        layout = QVBoxLayout()

        # Etiqueta con el nombre completo centrado
        self.name_label = QLabel('Nombre Completo: Blanca Leticia Argueta Portillo')
        self.name_label.setAlignment(Qt.AlignCenter)  # Centrar el texto
        layout.addWidget(self.name_label)

        # Etiqueta con la edad centrada
        self.age_label = QLabel('Edad: 19 años')
        self.age_label.setAlignment(Qt.AlignCenter)  # Centrar el texto
        layout.addWidget(self.age_label)

        # Configurar layout
        self.setLayout(layout)

# Inicializar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PersonalInfoWindow()
    window.show()
    sys.exit(app.exec_())
