class Chinela:
    def __init__(self):
        self.__tamanho=0

    def get_Tamanho(self):
        return self.__tamanho

    def set_Tamanho(self,value:int):
        if 20>value<50:
            print()


def main():
    chinela=Chinela()
    while chinela.get_Tamanho()==0:
        print("Digite seu tamanho de chinela")
        tamanho=int(input())
        chinela.set_Tamanho(tamanho)
    
    print(f"Parabéns, você comprou uma chinela tamanho,{chinela.get_Tamanho()}")
main()