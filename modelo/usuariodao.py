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
    
    def registrarUsuario(self, usuario, contrasena):
        try:
            self.bd.establecerConexionBD()
            cursor = self.bd.conexion.cursor()
            
            # Verificar si el usuario ya existe
            cursor.execute("SELECT COUNT(*) FROM usuarios WHERE usuario = ?", [usuario])
            existe = cursor.fetchone()[0]
            
            if existe > 0:
                self.bd.cerrarConexionBD()
                return False, "El usuario ya existe"
            
            # Insertar nuevo usuario
            sql = "INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)"
            cursor.execute(sql, [usuario, contrasena])
            self.bd.conexion.commit()
            self.bd.cerrarConexionBD()
            
            return True, "Usuario registrado exitosamente"
        except Exception as e:
            self.bd.cerrarConexionBD()
            return False, f"Error al registrar: {str(e)}"