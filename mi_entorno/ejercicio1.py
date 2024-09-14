import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette

class PersonalInfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle('Información Personal')
        self.setGeometry(100, 100, 400, 200)

        # Configuración del fondo de la ventana
        self.setStyleSheet("background-color: #f0f0f0;")  # Color de fondo

        # Layout principal
        layout = QVBoxLayout()
        layout.setSpacing(20)  # Espaciado entre widgets

        # Etiqueta con el nombre completo centrado
        self.name_label = QLabel('Nombre Completo: Blanca Leticia Argueta Portillo')
        self.name_label.setAlignment(Qt.AlignCenter)  # Centrar el texto
        self.name_label.setFont(QFont('Arial', 16, QFont.Bold))  # Fuente más grande y negrita
        self.name_label.setStyleSheet("color: #2e8b57;")  # Color de texto verde
        layout.addWidget(self.name_label)

        # Etiqueta con la edad centrada
        self.age_label = QLabel('Edad: 19 años')
        self.age_label.setAlignment(Qt.AlignCenter)  # Centrar el texto
        self.age_label.setFont(QFont('Arial', 16, QFont.Bold))  # Fuente más grande y negrita
        self.age_label.setStyleSheet("color: #4682b4;")  # Color de texto azul
        layout.addWidget(self.age_label)

        # Configurar layout
        self.setLayout(layout)

# Inicializar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PersonalInfoWindow()
    window.show()
    sys.exit(app.exec_())
