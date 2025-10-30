from PyQt5 import QtWidgets
import sys
from load.load_ui_productos import Load_ui_productos
from load.load_ui_login import Load_ui_login
from load.load_ui_menu import Load_ui_menu
def main():
    
    app = QtWidgets.QApplication(sys.argv)
    
    # Cargar ventana de login primero
    window1 = Load_ui_login()
    window1.show()
    
    #cargar ventana menu eleccion
    window2 = Load_ui_menu()
    #window2.show()

    window = Load_ui_productos()
    #window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()