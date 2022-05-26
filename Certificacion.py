from datetime import date


class Certificacion:
    FechaCertificacion:date
    Pares:str

    def BuscarCertificacion(self):
        print("Certificacion.")
    
    def ActualizarCertificacion(self):
        print("Se actualizo la Certificacion.")

        def main():
            Certificacion = str(input("Ingrese la certificacion : "))

            for i in range(Certificacion):
                outfile = open('Certificacion.txt','a')
                FechaCertificacion= input("Ingrese la fecha de la certificacion: ")
                Pares= input("Ingrese el par de la certificacion: ")
                outfile.write("Fecha de la certificacion: " + FechaCertificacion + "\n")
                outfile.write("ingrese el nombre del par: " + Pares + "\n\n")

        main()