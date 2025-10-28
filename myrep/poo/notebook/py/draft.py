class Notebook:
    def __init__(self):
        self.__ligado: bool=False
        
    def ligar(self):
        if self.__ligado is False:
            self.__ligado=True
            print("Notebook ligado")
        else:
            print("Notebook ja esta ligado")

    def desligar(self):
        if self.__ligado is True:
            self.__ligado=False
            print("Notebook desligado")
        else:
            print("Notebook ja esta desligado")
    
    def mostrar(self):
        status = "ligado" if self.__ligado else "desligado"
        print(f"O notebook está {status}.")

    
    def getLigado(self):
        return self.__ligado

    def __str__(self):
        status = "ligado" if self.__ligado else "desligado"
        return f"Notebook: {status}"
    
    
def main():
    notebook=Notebook()
    while True:
        line=input()
        print("$"+line)
        args=line.split()

        if args[0]=="end":
            break
        if args[0]=="show":
            print(notebook)
        if args[0]=="ligar":
            notebook.ligar()
        if args[0]=="desligar":
            notebook.desligar()


main()