class Pessoa:
    def __init__(self, name:str, age:int):
        self.__age=age
        self.__name=name

    def getAge(self):
        return self.__age
    
    def getname(self):
        return self.__name

    def __str__(self):
        return f"{self.__name}:{self.__age}"

class Moto:
    def __init__(self, pot: int = 1, tempo: int = 0):
        self.__pot = pot
        self.__tempo = tempo
        self.__pessoa = None 

    def getPessoa(self):
        if self.__pessoa is None:
            return "(empty)"
        return f"({self.__pessoa})"

    def entrar(self, name: str, age: int):
        if self.__pessoa is not None:
            print("fail: busy motorcycle")
        else:
            self.__pessoa = Pessoa(name, age) 

    def sair(self):
        if self.__pessoa is None:
            print("fail: empty motorcycle")
            return None
        else:
            pessoa_saiu = self.__pessoa
            self.__pessoa = None
            print(pessoa_saiu)  
            return pessoa_saiu
        
    def comprar(self, tempo: int):
        self.__tempo += tempo

    def honk(self):
        print("P" + "e" * self.__pot + "m")

    def drive(self,minutos:int):
        if self.__tempo<=0:
            print("fail: buy time first")
            return
        if self.__pessoa is None:
            print("fail: empty motorcycle")
            return
        
        if self.__pessoa.getAge()>10:
            print("fail: too old to drive")
            return
        if minutos>self.__tempo:
            print(f"fail: time finished after {self.__tempo} minutes")
            self.__tempo=0
        else:
            self.__tempo-=minutos

    def __str__(self):
        return f"power:{self.__pot}, time:{self.__tempo}, person:{self.getPessoa()}"

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
            moto = Moto(int(args[1]))
        if args[0]=="enter":
            moto.entrar(str(args[1]), int(args[2]))
        if args[0]=="leave":
            moto.sair()
        if args[0]=="buy":
            moto.comprar(int(args[1]))
        if args[0]=="drive":
            moto.drive(int(args[1]))
        if args[0]=="honk":
            moto.honk()
main()