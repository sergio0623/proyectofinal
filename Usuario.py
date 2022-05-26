from inspect import _void


class Usuario:
    Id:str
    Nombre:str
    TipoContratacion:str
    MaximoNivelFormacion:str
    HorasDedicacion:str
    Cargo:str
    
              
    def ActualizarUsuario(self):
       print("Se actualizo el Usuario")
       
    def CrearUsuario(self):
        print("Se creo Usuario")
        
    def main():
            Usuario= int(input("Ingrese el Usuario: "))
            
            for i in range(Usuario):
                outfile = open('Usuarios.txt','a')
                Nombre = input("Ingrese el nombre del Usuario: ")
                TipoContratacion= input("Ingrese el Tipo de Contratación: ")
                outfile.write("Nombre del Usuario: " + Nombre + "\n")
                outfile.write("Tipo de  Contratación: " +TipoContratacion + "\n\n")
                
    main()