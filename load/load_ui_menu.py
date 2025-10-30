import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets, uic  
from PyQt5.QtWidgets import QTableWidgetItem
from modelo.productodao import ProductoDAO
from load.load_ui_productos import Load_ui_productos
from load.load_ui_clientes import Load_ui_clientes

class Load_ui_menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar archivo .ui
        uic.loadUi("ui/ui_menu.ui", self)
        self.resize(1200, 800)
        #self.show()

        self.load_productos_btn.clicked.connect(self.abrir_productos)
        self.load_clientes_btn.clicked.connect(self.abrir_clientes)


    def abrir_productos(self):
        self.ventana_productos = Load_ui_productos()
        self.ventana_productos.show()
        self.close()  # Cerrar ventana de login


    def abrir_clientes(self):
        self.ventana_clientes = Load_ui_clientes()
        self.ventana_clientes.show()
        self.close()  # Cerrar ventana de login