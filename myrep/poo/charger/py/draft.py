class Bateria:
    def __init__(self, capacidade: int) :
        self._capacidade = capacidade
        self._carga = capacidade
    def getcapacidade(self) -> int:
        return self._capacidade
    def consumir(self, minutos: int) -> int:
        usado = min(minutos, self._carga)
        self._carga -= usado
        return usado
    def carregar(self, minutos :int,potencia: int) -> None:
        self._carga = min (self._capacidade, self._carga + minutos * potencia)
    def mostrar(self) -> None:
        print(f"{self._carga}/{self._capacidade}")
class Carregador:
    def __init__(self,potencia: int):
        self._potencia = potencia
class Notebook:
    def __init__(self):
        self._ligado = Falseself._