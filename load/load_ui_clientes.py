#1.- Importar librerias
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets, uic  
from PyQt5.QtWidgets import QTableWidgetItem
from modelo.empleadodao import ClientesDao


#2.- Cargar archivo .ui
class Load_ui_clientes(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar archivo .ui
        uic.loadUi("ui/ui_clientes.ui", self)
        self.resize(1200, 800)

        #3.- Configurar contenedores
        #eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        # Fijar ancho columnas
        self.tabla_consulta.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        #4.- Inicializar modelo de datos
        self.clientesdao = ClientesDao()

        #5.- Conectar botones a funciones
        self.conectar_botones()

        # Cargar datos iniciales
        self.actualizar_tabla()

    def conectar_botones(self):
        """Conectar todos los botones a sus funciones correspondientes"""
        
        # Botones para cambiar de página
        self.boton_agregar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_agregar))
        self.boton_buscar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_buscar))
        self.boton_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        self.boton_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
        self.boton_consultar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_consultar))

        # Botones de acciones CRUD
        self.accion_guardar.clicked.connect(self.guardar_clientes)
        self.accion_actualizar.clicked.connect(self.actualizar_clientes)
        self.accion__eliminar.clicked.connect(self.eliminar_clientes)
        self.accion_limpiar.clicked.connect(self.limpiar_clientes)
        self.buscar_actualizar.clicked.connect(self.buscar_clientes_actualizar)
        self.buscar_eliminar.clicked.connect(self.buscar_clientes_eliminar)
        self.buscar_buscar.clicked.connect(self.buscar_clientes_buscar)
        self.boton_refresh.clicked.connect(self.actualizar_tabla)

        # Botones de navegación y menú
        self.boton_salir.clicked.connect(self.abrir_login)
        self.boton_menu.clicked.connect(self.mover_menu)

    def abrir_login(self):
        """Abrir ventana de login y cerrar actual"""
        from load.load_ui_login import Load_ui_login
        self.ventana_login = Load_ui_login()
        self.ventana_login.show()
        self.close()

#5.- Operaciones con el modelo de datos 
    def actualizar_tabla(self):
        try:
            clientes = self.clientesdao.listarClientes()
            self.tabla_consulta.clearContents()
            self.tabla_consulta.setRowCount(len(clientes))
            self.tabla_consulta.setColumnCount(4)
            self.tabla_consulta.setHorizontalHeaderLabels(['SKU Clientes', 'Cargo', 'Nombre', 'Edad'])
            
            for fila, cliente in enumerate(clientes):
                self.tabla_consulta.setItem(fila, 0, QTableWidgetItem(str(cliente[0])))
                self.tabla_consulta.setItem(fila, 1, QTableWidgetItem(str(cliente[1])))
                self.tabla_consulta.setItem(fila, 2, QTableWidgetItem(str(cliente[2])))
                self.tabla_consulta.setItem(fila, 3, QTableWidgetItem(str(cliente[3])))

            self.tabla_consulta.resizeColumnsToContents()
        except Exception as e:
            print(f"Error al actualizar tabla: {e}")

    def buscar_clientes_actualizar(self):
        try:
            self.clientesdao.clientes.id_employee = self.sku_actualizar.text()
            datos = self.clientesdao.buscarClientes()
        
            if len(datos) > 0:
                self.cargo_actualizar.setText(str(datos[0][0]))
                self.nombre_actualizar.setText(str(datos[0][1]))
                self.edad_actualizar.setText(str(datos[0][2]))
            else:
                print("Cliente no encontrado")
        except Exception as e:
            print(f"Error al buscar cliente: {e}")

    def buscar_clientes_eliminar(self):
        try:
            self.clientesdao.clientes.id_employee = self.sku_eliminar.text()
            datos = self.clientesdao.buscarClientes()
        
            if len(datos) > 0:
                self.cargo_eliminar.setText(str(datos[0][0]))
                self.nombre_eliminar.setText(str(datos[0][1]))
                self.edad_eliminar.setText(str(datos[0][2]))
            else:
                print("Cliente no encontrado")
        except Exception as e:
            print(f"Error al buscar cliente: {e}")

    def buscar_clientes_buscar(self):
        try:
            self.clientesdao.clientes.id_employee = self.sku_buscar.text()
            datos = self.clientesdao.buscarClientes()
        
            if len(datos) > 0:
                self.cargo_buscar.setText(str(datos[0][0]))
                self.nombre_buscar.setText(str(datos[0][1]))
                self.edad_buscar.setText(str(datos[0][2]))
            else:
                print("Cliente no encontrado")
        except Exception as e:
            print(f"Error al buscar cliente: {e}")

    def guardar_clientes(self):
        try:
            self.clientesdao.clientes.id_employee = self.sku_agregar.text()
            self.clientesdao.clientes.cargo = self.cargo_agregar.text()
            self.clientesdao.clientes.nombre = self.nombre_agregar.text()
            self.clientesdao.clientes.edad = int(self.edad_agregar.text())

            self.clientesdao.insertarClientes()
            self.actualizar_tabla()
            self.limpiar_campos_agregar()
            print("Cliente guardado exitosamente")
        except Exception as e:
            print(f"Error al guardar cliente: {e}")

    def limpiar_campos_agregar(self):
        """Limpiar campos de la página agregar"""
        self.sku_agregar.clear()
        self.cargo_agregar.clear()
        self.nombre_agregar.clear()
        self.edad_agregar.clear()

    def limpiar_clientes(self):
        """Limpiar campos de la página buscar"""
        self.sku_buscar.clear()
        self.cargo_buscar.clear()
        self.nombre_buscar.clear()
        self.edad_buscar.clear()

    def actualizar_clientes(self):
        try:
            self.clientesdao.clientes.id_employee = self.sku_actualizar.text()
            self.clientesdao.clientes.cargo = self.cargo_actualizar.text()
            self.clientesdao.clientes.nombre = self.nombre_actualizar.text()
            self.clientesdao.clientes.edad = int(self.edad_actualizar.text())

            self.clientesdao.actualizarClientes()
            self.actualizar_tabla()
            print("Cliente actualizado exitosamente")
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")

    def eliminar_clientes(self):
        try:
            self.clientesdao.clientes.id_employee = self.sku_eliminar.text()
            self.clientesdao.eliminarClientes()
            self.actualizar_tabla()
            print("Cliente eliminado exitosamente")
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")

# 6.- mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

#7.- Mover menú
    def mover_menu(self):
        width = self.frame_lateral.width()
        normal = 0
        
        if width == 0:
            extender = 200
            self.boton_menu.setText("Menú")
        else:
            extender = normal
            self.boton_menu.setText("")
            
        self.animacion = QPropertyAnimation(self.frame_lateral, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()