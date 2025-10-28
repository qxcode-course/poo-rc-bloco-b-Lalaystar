class Bateria:
    def __init__(self,carg:int,pot:int):
        self.__carg=carg
        self.__pot=pot

    def gastar(self,tempo:int):
        gasto = min(self.__carg, tempo)
        self.__carg-= gasto
        return gasto 

class Carregador:
    def __init__(self, pot:int):
        self.potencia = pot

    def __str__(self):
        return f"Potência: {self.potencia}"


class Notebook:
    def __init__(self):
        self.__ligado = False

    def turn_on(self):
        if not self.__ligado:
            self.__ligado = False
            print("fail: não foi possível ligar")
        else:
            print("Notebook ligado")

    def turn_off(self):
        if self.__ligado:
            self.__ligado = False
            print("Notebook desligado")
        else:
            print("fail: não foi possível desligar")  

    def usar(self, tempo:int):
        if self.__ligado:
            print(f"Usando o notebook por {tempo} minutos")
        else:
            print("fail: desligado")

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
        if args[0]=="turn_on":
            notebook.turn_on()
        if args[0]=="desligar":
            notebook.turn_off()
        if args[0]=="use":
            tempo = int(args[1])
            notebook.usar(tempo)

main()