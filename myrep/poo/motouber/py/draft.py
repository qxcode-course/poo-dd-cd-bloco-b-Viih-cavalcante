class Peesoa:
    def __init__(self, name : str, money :int):
        self._name : str = name
        self._money: int = money
    def getName(self) -> str:
        return self._name
    def getMoney(self)-> int:
        return self._money
    def setMoney(self, valor : int)-> int:
        self._money = valor
    def pagar(self, valor: int) -> int:
        self.__money -= valor
    def receber(self, valor: int) ->:
        self._money += valor
    def __str__(self)-> str:
        return f"{self.getName()}:{self.getMoney()}"
    



def main():
        moto=Moto(0)
        while True:
            line = input()
            print("$ + line")
            args = line.split()
            if args [0] =="end" :
                break
            if args[0] == "show":
                print(moto)
            if args[0] == "setDriver":
                name = args[1]
                money = int(args[2])
                motorista = Pessoa(name, money)
                moto.setDriver(motorista)
            elif args[0] == "setPass":
                name = args[1]
                money = int(args[2])
                passageiro = Pessoa(name, money)
                moto.setPass(passageiro)
            elif args[0] == "drive":
                km = int(args[1])
                moto.dirigir(km)
            elif args[0] == "leavePass":
                moto.descer()
main()