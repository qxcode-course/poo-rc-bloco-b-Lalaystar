class Relogio:
    def __init__(self, hora:int=0,minuto:int=0,segundo:int=0):
        self.__hora= 0
        self.__minuto=0
        self.__segundo=0
        self.setHora(hora)
        self.setMinuto(minuto)
        self.setSegundo(segundo)

    def getHora(self):
        return self.__hora
    def getMinuto(self):
        return self.__minuto
    def getSegundo(self):
        return self.__segundo
    
    def setHora(self, hora: int):
        if 0<=hora<=23:
            self.__hora=hora
        else:
            print("fail: hora invalida")

    def setMinuto(self,minuto:int):
        if 0<=minuto<=59:
            self.__minuto=minuto
        else:
            print("fail: minuto invalida")
    
    def setSegundo(self, segundo:int):
        if 0<=segundo<=59:
            self.__segundo=segundo
        else:
            print("fail: segundo invalido")

    def nextSecond(self):
        self.__segundo+=1
        if self.__segundo==60:
            self.__segundo=0
            self.__minuto+=1
        if self.__minuto==60:
            self.__minuto=0
            self.__hora+=1
        if self.__hora==0:
            self.__hora=0

    def __str__(self)->str:
        return f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}"

def main():
    relogio=Relogio(00,00,00)
    while True:
        line=input()
        print("$"+line)
        args=line.split()
        
        if args[0]=="end":
            break
        if args[0]=="show":
            print(relogio)

main()