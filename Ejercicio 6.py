import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QSpinBox, QPushButton, QMessageBox
#Este programa permite a los usuarios seleccionar su nivel de actividad física (Bajo, Moderado o Alto) utilizando botones de radio (QRadioButton). Además, permite ingresar cuántas horas de ejercicio hacen por semana con un QSpinBox, que tiene un rango entre 0 y 40 horas. 
class ActividadFisicaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Actividad Física")

        layout_principal = QVBoxLayout()

        self.label_nivel = QLabel("Selecciona tu nivel de actividad física:")
        self.radio_bajo = QRadioButton("Bajo")
        self.radio_moderado = QRadioButton("Moderado")
        self.radio_alto = QRadioButton("Alto")

        layout_principal.addWidget(self.label_nivel)
        layout_principal.addWidget(self.radio_bajo)
        layout_principal.addWidget(self.radio_moderado)
        layout_principal.addWidget(self.radio_alto)

        self.label_horas = QLabel("¿Cuántas horas de ejercicio haces por semana?")
        self.spin_horas = QSpinBox()
        self.spin_horas.setRange(0, 40)   

       
        layout_principal.addWidget(self.label_horas)
        layout_principal.addWidget(self.spin_horas)

        
        self.boton_mostrar = QPushButton("Mostrar Datos")
        self.boton_mostrar.clicked.connect(self.mostrar_datos)

        
        layout_principal.addWidget(self.boton_mostrar)

        
        self.setLayout(layout_principal)

    def mostrar_datos(self):
        
        if self.radio_bajo.isChecked():
            nivel_actividad = "Bajo"
        elif self.radio_moderado.isChecked():
            nivel_actividad = "Moderado"
        elif self.radio_alto.isChecked():
            nivel_actividad = "Alto"
        else:
            nivel_actividad = "No seleccionado"

        
        horas_ejercicio = self.spin_horas.value()

      
        mensaje = f"Nivel de actividad física: {nivel_actividad}\nHoras de ejercicio por semana: {horas_ejercicio}"
        QMessageBox.information(self, "Datos Ingresados", mensaje)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    
    ventana = ActividadFisicaApp()
    ventana.show()

    
    sys.exit(app.exec_())
