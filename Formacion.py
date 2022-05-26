from datetime import date


class Formacion:
    CodFormacion: str
    TipoFormacion: str
    NombreFormacion: str
    
    
        
   
    def BuscarFormacion(self):
           print("Se encontro lo siguiente:")
   
    def DefinirFormacion(self):
           print("Su Nivel de Formación es")
         
     
    def main():
            Formacion= int(input("Ingrese la Formación: "))
            
            for i in range(Formacion):
                outfile = open('Formaciones.txt','a')
                CodFormacion= input("Ingrese el Codigo de Formación: ")
                TipoFormacion= input("Ingrese el Tipo de Formación : ")
                NombreFormacion= input("Ingrese el Nombre de la Formación : ")
                outfile.write("Codigo de la Formación: " + CodFormacion + "\n")
                outfile.write("Tipo de Formación: " +TipoFormacion + "\n")
                outfile.write("Nombre de la Formación: " +NombreFormacion + "\n\n")
                
    main()