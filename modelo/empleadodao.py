from modelo.empleado import Empleado
from modelo.conexionbd import ConexionBD

class ClientesDao:
    def __init__(self):
        self.bd = ConexionBD()
        self.clientes = Empleado()
        
    def listarClientes(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_listar_empleados]'
        cursor.execute(sp)
        filas = cursor.fetchall()
        self.bd.cerrarConexionBD()
        return filas 
    
    def buscarClientes(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_buscar_empleado] @id_employee=?'
        param = [self.clientes.id_employee]
        cursor.execute(sp, param) 
        filas = cursor.fetchall()
        self.bd.cerrarConexionBD()
        return filas 

    def insertarClientes(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_insertar_empleado]@id_employee=?,@cargo=?,@nombre=?,@edad=?'
        param = (self.clientes.id_employee,self.clientes.cargo,self.clientes.nombre,self.clientes.edad)
        cursor.execute(sp, param)
        self.bd.conexion.commit()
        self.bd.cerrarConexionBD()

    def actualizarClientes(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_actualizar_empleado] @id_employee=?,@cargo=?,@nombre=?,@edad=?'
        param = (self.clientes.id_employee,self.clientes.cargo,self.clientes.nombre,self.clientes.edad)
        cursor.execute(sp, param)
        self.bd.conexion.commit()
        self.bd.cerrarConexionBD()

    def eliminarClientes(self):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_eliminar_empleado] @id_employee=?'
        cursor.execute(sp, self.clientes.id_employee)
        self.bd.conexion.commit()
        self.bd.cerrarConexionBD()
