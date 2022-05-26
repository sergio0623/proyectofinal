from curses.ascii import ESC
from Escalafon import Escalafon
from ExperienciaProfesional import ExperienciaProfesional


class Docente(Usuario):
    experienciaInvestigacion=ExperienciaInvestigacion
    apoyo=Apoyo
    grupoInvestigacion=GrupoInvestigacion
    laborExtracurricular=LaborExtracurricular

    def __init__(self,experienciaProfesional:ExperienciaProfesional, experienciaDocente:ExperienciaDocente, escalafon:Escalafon, formacion:Formacion):
        self.ExperienciaProfesional=experienciaProfesional
        self.ExperienciaDocente = experienciaDocente
        self.Escalafon = escalafon
        self.Formacion = formacion

    def BuscarDocente(self):
        print("BuscarDocente.")

    def InactivarDocente(self):
        print("Desactivado")

    def ActualizarDocente(self):
        print("Actualizado")
    

        def main():
            Docente= int(input("Ingrese la certificacion: "))

            for i in range(Docente):
                outfile = open('Docente.txt','a')
                NombreDocente= input("Ingrese el nombre del docente: ")
                outfile.write("Ingrese el nombre del docente: " + NombreDocente + "\n""\n")

        main()