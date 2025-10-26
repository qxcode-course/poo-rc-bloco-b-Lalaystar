class Moto:
    def __init__(self,pot:int=1, tempo:int=0, pessoa:int=0):
        self.__pot=1
        self.__tempo=0
        self.__pessoa="(empty)"
        self.setPot(pot)
        self.setTempo(tempo)
        self.setPessoa(pessoa)

    def getPot(self):
        return self.__pot
    def getTempo(self):
        return self.__tempo
    def getPessoa(self):
        return self.__pessoa
    
    def setPot(self, pot:int):
        if pot>0:
            self.__pot=pot
        else:
            print("fail: potencia invalida")
        
    def setTempo(self, tempo:int):
        if tempo>=0:
                self.__tempo=tempo
        else:
                print("fail: tempo invalido")

    def setPessoa(self, pessoa:int):
        if pessoa == 0:
            self.__pessoa = "(empty)"
        elif 1 <= pessoa <= 2:
            self.__pessoa = pessoa
        else:
            print("fail: numero de pessoas invalido")

    def entrar(self):
        if self.__pessoa!="(empty)":
            print("fail: moto ocupada")
        else:
            self.__pessoa=1

    def sair(self):
        if self.__pessoa=="(empty)":
            print("fail: moto vazia")
        else:
            self.__pessoa="(empty)"

    def comprar(self):
        
    def __str__(self)->str:
        return f"power:{self.__pot}, time:{self.__tempo}, person:{self.__pessoa}"

def main():
    moto=Moto()
    while True:
        line=input()
        print("$"+line)
        args=line.split()

        if args[0]=="end":
            break
        if args[0]=="show":
            print(moto)
        if args[0]=="init":
            moto=Moto(int(args[1]), int(args[2]), int(args[3]))
        if args[0]=="enter":
            moto.entrar()
        if args[0]=="leave":
            moto.sair()

main()