from datetime import date
from sqlite3 import Date


class LaborExtracurricular:
    LugarDesempeno: str
    Cargo: str
    FechaLabor: date
    
    
    def BuscarLaborExtracurricular(self):
         print("Se encontraron los datos:")
         
         
    def main():
            LaborExtracurricular= int(input("Ingrese la labor Extracurricular del Docente: "))
            
            for i in range(LaborExtracurricular):
                outfile = open('LaborExtracurricular.txt','a')
                LugarDesempeno = input("Ingrese el Lugar de Desempeño: ")
                Cargo= input("Ingrese el Cargo Desempeñado: ")
                outfile.write("Lugar de desempeño: " + LugarDesempeno + "\n")
                outfile.write("Cargo: " +Cargo + "\n\n")
                
    main()