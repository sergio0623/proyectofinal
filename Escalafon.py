class Escalafon:
    CodEscalafon:str
    TipoEscalafon:str
        
    def BuscarEscalafon(self):
        print("BuscarEscalafon. ")

    def DefinirEscalafon(self):
        print("SeDefinio. ")

    def main():
        Escalafon = int(input("Ingrese el escalafon: "))

        for i in range(Escalafon):
            outfile = open('Escalafon.txt','a')
            CodigoEscalafon = input("Ingrese el codigo del escalafon: ")
            TipoEscalafon= input("Ingrese el tipo del escalafon: ")
            outfile.write("Codigo del escalafon: " + CodigoEscalafon + "\n")
            outfile.write("Tipo escalafon: " + TipoEscalafon + "\n\n")


    main()
