class Pessoa:
    def __init__(self, name: str, money: int):
        self._name: str = name
        self._money: int = money
    def getName(self) -> str:
        return self._name
    def getMoney(self) -> int:
        return self._money
    def setMoney(self, valor: int):
        self._money = valor
    def pagar(self, valor: int):
        self._money -= valor
    def receber(self, valor: int):
        self._money += valor
    def __str__(self) -> str:
        return f"{self.getName()}:{self.getMoney()}"
class Moto:
    def __init__(self,custo :int):
        self._custo: int = custo
        self._motorista: Pessoa | None = None
        self._passageiro: Pessoa | None =None
    def getCusto(self) -> int:
        return self._custo
    def getDriver(self) -> Pessoa | None:
        return self._motorista
    def setDriver(self, motorista: Pesssoa):
        self._motorista = motorista
    def getPass(self,passageiro: Pessoa):
        self._motoristrta = motorista
    def setPass(self, passageiro: Pessoa):
        self._passageiro = passageiro
    def subir(self, passageiro: Pessoa):
        if self._motorista == None:
            print("fail: moto ja tem passageiro")
            return
        self._passageiro = passageiro
    def descer(self):
        if self.getPasss().getMoney() < self.getCusto():

    



def main():
    moto = Moto(0)
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
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