class Camisa:
    def _init_(self):
        self.__tamanho: str= ""

    def getTamanho(self) -> str:
        return self.__tamanho
    
    def setTamanho(self,valor:str):
        tamv=["PP", "P", "M", "G", "GG", "XG"]
        if valor in tamv:
            self.__tamanho=valor
        else:
            print("tamanho errado")
    
    def __str__(self):
        if self.__tamanho == "":
            return "size: ()"
        else:

            return f"size: ({self.__tamanho})"


def main():
    camisa=Camisa()
    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(camisa)
        elif args[0] == "size":
            camisa.setTamanho(args[1])
        else:
            print("fail: comando invalido")
main()
