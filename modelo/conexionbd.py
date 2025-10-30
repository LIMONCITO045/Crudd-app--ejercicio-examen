import pyodbc

class ConexionBD:
    def __init__(self):
        self.conexion=''

    def establecerConexionBD(self):
        try:
            #DRIVER={SQL Server};TIZIENA\MISQLJULIANSERV\SQLEXPRESS;DATABASE=bdsistema;UID=sa;PWD=Password01
            self.conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=TIZIENA\MISQLJULIANSERV;DATABASE=bdsistema;Trusted_Connection=yes;')
            print ("Conexion establecida")
        except Exception as ex:
            print("Error de conexion : " + ex)


    def cerrarConexionBD(self):
        self.conexion.close()
        