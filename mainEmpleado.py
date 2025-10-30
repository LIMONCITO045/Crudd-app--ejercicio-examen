from modelo.empleadodao import EmpleadoDAO
def main():
    empleadodao= EmpleadoDAO()
    empleadodao.insertarEmpleado()
    empleadodao.listarEmpleado()  
    
   # empleadodao.actualizarEmpleado()
    #empleadodao.eliminarEmpleado()
  
if __name__=="__main__":
    main()
