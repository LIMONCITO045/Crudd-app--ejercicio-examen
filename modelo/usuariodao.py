from modelo.conexionbd import ConexionBD

class UsuarioDAO:
    def __init__(self):
        self.bd = ConexionBD()
    
    def validarUsuario(self, usuario, contrasena):
        self.bd.establecerConexionBD()
        cursor = self.bd.conexion.cursor()
        
        sp = 'exec [dbo].[sp_ValidarUsuario] @usuario=?, @contrasena=?'
        param = [usuario, contrasena]
        cursor.execute(sp, param)
        
        resultado = cursor.fetchone()
        self.bd.cerrarConexionBD()
        
        # Si el resultado es 1, el usuario es válido
        if resultado and resultado[0] == 1:
            return True
        else:
            return False
    
    