#1.- Importar librerias
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets, uic  
from PyQt5.QtWidgets import QTableWidgetItem
from modelo.productodao import ProductoDAO


#2.- Cargar archivo .ui
class Load_ui_productos(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar archivo .ui
        uic.loadUi("ui/ui_productos.ui", self)
        self.resize(1200, 800)

        #3.- Configurar contenedores
        #eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        # Fijar ancho columnas
        self.tabla_consulta.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        #4.- Inicializar modelo de datos
        self.productodao = ProductoDAO()

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
        self.accion_guardar.clicked.connect(self.guardar_producto)
        self.accion_actualizar.clicked.connect(self.actualizar_producto)
        self.accion__eliminar.clicked.connect(self.eliminar_producto)
        self.accion_limpiar.clicked.connect(self.limpiar_producto)
        self.buscar_actualizar.clicked.connect(self.buscar_producto_actualizar)
        self.buscar_eliminar.clicked.connect(self.buscar_producto_eliminar)
        self.buscar_buscar.clicked.connect(self.buscar_producto_buscar)
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
            productos = self.productodao.listarProductos()
            self.tabla_consulta.clearContents()
            self.tabla_consulta.setRowCount(len(productos))
            self.tabla_consulta.setColumnCount(4)
            self.tabla_consulta.setHorizontalHeaderLabels(['SKU', 'Descripción', 'Existencia', 'Precio'])
            
            for fila, producto in enumerate(productos):
                self.tabla_consulta.setItem(fila, 0, QTableWidgetItem(str(producto[0])))
                self.tabla_consulta.setItem(fila, 1, QTableWidgetItem(str(producto[1])))
                self.tabla_consulta.setItem(fila, 2, QTableWidgetItem(str(producto[2])))
                self.tabla_consulta.setItem(fila, 3, QTableWidgetItem(str(producto[3])))

            self.tabla_consulta.resizeColumnsToContents()
        except Exception as e:
            print(f"Error al actualizar tabla: {e}")

    def buscar_producto_actualizar(self):
        try:
            self.productodao.producto.clave = self.sku_actualizar.text()
            datos = self.productodao.buscarProducto()
        
            if len(datos) > 0:
                self.descripcion_actualizar.setText(str(datos[0][0]))
                self.existencia_actualizar.setText(str(datos[0][1]))
                self.precio_actualizar.setText(str(datos[0][2]))
            else:
                print("Producto no encontrado")
        except Exception as e:
            print(f"Error al buscar producto: {e}")

    def buscar_producto_eliminar(self):
        try:
            self.productodao.producto.clave = self.sku_eliminar.text()
            datos = self.productodao.buscarProducto()
        
            if len(datos) > 0:
                self.descripcion_eliminar.setText(str(datos[0][0]))
                self.existencia_eliminar.setText(str(datos[0][1]))
                self.precio_eliminar.setText(str(datos[0][2]))
            else:
                print("Producto no encontrado")
        except Exception as e:
            print(f"Error al buscar producto: {e}")

    def buscar_producto_buscar(self):
        try:
            self.productodao.producto.clave = self.sku_buscar.text()
            datos = self.productodao.buscarProducto()
        
            if len(datos) > 0:
                self.descripcion_buscar.setText(str(datos[0][0]))
                self.existencia_buscar.setText(str(datos[0][1]))
                self.precio_buscar.setText(str(datos[0][2]))
            else:
                print("Producto no encontrado")
        except Exception as e:
            print(f"Error al buscar producto: {e}")

    def guardar_producto(self):
        try:
            self.productodao.producto.clave = self.sku_agregar.text()
            self.productodao.producto.descripcion = self.descripcion_agregar.text()
            self.productodao.producto.existencia = int(self.existencia_agregar.text())
            self.productodao.producto.precio = float(self.precio_agregar.text())

            self.productodao.insertarProducto()
            self.actualizar_tabla()
            self.limpiar_campos_agregar()
            print("Producto guardado exitosamente")
        except Exception as e:
            print(f"Error al guardar producto: {e}")

    def limpiar_campos_agregar(self):
        """Limpiar campos de la página agregar"""
        self.sku_agregar.clear()
        self.descripcion_agregar.clear()
        self.existencia_agregar.clear()
        self.precio_agregar.clear()

    def limpiar_producto(self):
        """Limpiar campos de la página buscar"""
        self.sku_buscar.clear()
        self.descripcion_buscar.clear()
        self.existencia_buscar.clear()
        self.precio_buscar.clear()

    def actualizar_producto(self):
        try:
            self.productodao.producto.clave = self.sku_actualizar.text()
            self.productodao.producto.descripcion = self.descripcion_actualizar.text()
            self.productodao.producto.existencia = int(self.existencia_actualizar.text())
            self.productodao.producto.precio = float(self.precio_actualizar.text())

            self.productodao.actualizarProducto()
            self.actualizar_tabla()
            print("Producto actualizado exitosamente")
        except Exception as e:
            print(f"Error al actualizar producto: {e}")

    def eliminar_producto(self):
        try:
            self.productodao.producto.clave = self.sku_eliminar.text()
            self.productodao.eliminarProducto()
            self.actualizar_tabla()
            print("Producto eliminado exitosamente")
        except Exception as e:
            print(f"Error al eliminar producto: {e}")

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