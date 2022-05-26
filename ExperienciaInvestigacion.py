class ExperienciaInvestigacion:
    AnosInvestigacion: int 
    CantidadPublicaciones: int
    TipoPublicacion: str
    
    
    
      
    
    
    def BuscarExperienciaInvestigacion(self):
         print("Se encontraron los resultados")
        
   
    def ActualizarExperienciaInvestigacion(self):
         print("Se actualizaron los datos")
         
         
    def main():
         ExperienciaInvestigacion= int(input("Ingrese la Experiencia de Investigación: "))
         for i in range(ExperienciaInvestigacion):
              
              outfile = open('ExperinciaInvestigacion.txt','a')
              AnosInvestigacion= input("Ingrese Año de Investigación: ")
              CantidadPublicaciones= input("Ingrese la cantidad de Publicaciones : ")
              TipoPublicacion= input("Ingrese el Tipo de Publicaiones: ")
              outfile.write("Años de Investigación: " + AnosInvestigacion + "\n")
              outfile.write("Cantidad de Publicaciones: " +CantidadPublicaciones + "\n")
              outfile.write("Tipo de Publicaciones: " +TipoPublicacion + "\n\n")
                
    main()
         
         
     
    
