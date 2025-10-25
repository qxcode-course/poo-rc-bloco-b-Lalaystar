class Chinela:
    def __init__(self):
        self.__tamanho=0

    def get_Tamanho(self):
        return self.__tamanho

    def set_Tamanho(self,value:int):
        if value<20 or value>50:
            print("ta errado")
            return 
        elif value%2!=0:
            print("errou bixa")
            return 
        self.__tamanho=value

    def __str__(self):
        return(f"sua chinela é tamanho {self.__tamanho}")

def main():
    chinela=Chinela()
    print("Digite seu tamanho de chinela")
    tamanho=int(input())
    chinela.set_Tamanho(tamanho)
    while True:
        line=input()
        print("$"+line)
        args=line.split()

        if args[0]=="end":
            break
        if args[0]=="show":
            print(chinela)
            print(f"Parabéns, você comprou uma chinela tamanho, {chinela.get_Tamanho()}")

main()