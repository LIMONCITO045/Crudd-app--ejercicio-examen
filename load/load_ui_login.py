import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets, uic  
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from modelo.productodao import ProductoDAO
from modelo.usuariodao import UsuarioDAO
from load.load_ui_menu import Load_ui_menu

class Load_ui_login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar archivo .ui
        uic.loadUi("ui/ui_login.ui", self)
        self.resize(1200, 800)
        
        # Crear instancia del DAO de usuarios
        self.usuariodao = UsuarioDAO()
        
        # Deshabilitar el botón de login al inicio
        self.login_btn.setEnabled(False)
        
        # Conectar campos de texto para validar
        self.username_txt.textChanged.connect(self.validar_campos)
        self.password_txt.textChanged.connect(self.validar_campos)
        
        # Conectar botón de login
        self.login_btn.clicked.connect(self.validar_login)

    def validar_campos(self):
        # Obtener el texto de los campos
        usuario = self.username_txt.text().strip()
        contrasena = self.password_txt.text().strip()
        
        # Habilitar botón solo si ambos campos tienen texto
        if usuario and contrasena:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

    def validar_login(self):
        # Obtener credenciales
        usuario = self.username_txt.text().strip()
        contrasena = self.password_txt.text().strip()
        
        # Validar con la base de datos
        if self.usuariodao.validarUsuario(usuario, contrasena):
            # Login exitoso
            self.abrir_menu()
        else:
            # Login fallido
            QMessageBox.warning(self, "Error de Login", 
                               "Usuario o contraseña incorrectos.")
            # Limpiar campo de contraseña
            self.password_txt.clear()
            self.password_txt.setFocus()

    def abrir_menu(self):
        self.ventana_menu = Load_ui_menu()
        self.ventana_menu.show()
        self.close()  # Cerrar ventana de login