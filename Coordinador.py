class Coordinador(Usuario):
    Funciones:str


    def CrearUsuario(self):
        print("se creo el Coordinador con exito")
        
    def BuscarCoordinador(self):
        print("Coordinador")

        def main():
            Coordinador= int(input("Ingrese el número de actividades: "))

            for i in range(Coordinador):
                outfile = open('Coordinador.txt','a')
                NombredeCoodinador = input("Ingrese el nombre del Coordinador: ")
                Funciones= input("Ingrese las funciones: ")
                outfile.write("Nombre del Coordinador: " + NombredeCoodinador + "\n")
                outfile.write("Ingrese las funciones: " + Funciones + "\n\n")


        main()
