class Grupo:
    CodGrupo:str
    NomGrupo:str

        
    def CrearGrupo(self):
        print("Se creo grupo. ")

    def DefinirGrupo(self):
        print("Grupo definido. ")

    def ModificarGrupo(self):
        print("Modificado. ")
    
        def main():
            Grupo= int(input("Ingrese el grupo: "))

            for i in range(Grupo):
                outfile = open('Grupo.txt','a')
                NombreGrupo = input("Ingrese el nombre del grupo: ")
                CodigoGrupo= input("Ingrese el código del grupo: ")
                outfile.write("Nombre del Grupo: " + NombreGrupo + "\n")
                outfile.write("Codigo Grupo: " +CodigoGrupo + "\n\n")

        main()
