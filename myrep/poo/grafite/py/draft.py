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
    def pagar
