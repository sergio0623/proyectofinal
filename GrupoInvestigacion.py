from datetime import date
from sqlite3 import Date


class GrupoInvestigacion:
    NombreGrupo:str
    FechaGrupoInvestigacion:date
    
    
    def BuscarGrupoInvestigacion(self):
         print("Se encontraron los datos:")
    
    def ActualizarGrupoInvestigacion(self):
        print("Se actualizaron Correctamente")
        
        
    def main():
            GrupoInvestigacion= int(input("Ingrese el Grupo de Investigación: "))
            
            for i in range(GrupoInvestigacion):
                outfile = open('GruposInvestigacion.txt','a')
                NombreGrupo = input("Ingrese el Nombre del Grupo de Investigación: ")
                FechaGrupo= input("Ingrese la fecha de ingreso: ")
                outfile.write("Nombre del Grupo: " + NombreGrupo + "\n")
                outfile.write("Fecha de Ingreso: " +FechaGrupo + "\n\n")
                
    main()
   
     
   