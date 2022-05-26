class Estudiantes:
    CodEstudiante:str
    
    def __init__(self,asignatura:Asignatura,programa:Programa):
        self.Asignatura=asignatura
        self.Programa = programa

    def BuscarEstudiante(self):
        print("BuscarEstudiante. ")