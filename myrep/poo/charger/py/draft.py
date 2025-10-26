import sys, io, os

sys.stdout = io.TextIOWrapper(os.fdopen(sys.stdout.fileno(), "wb"), encoding="utf-8")
class Bateria:
    def __init__(self, capacidade: int) :
        self._capacidade = capacidade
        self._carga = capacidade
    def getCarga(self) -> int:
        return self._carga
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
    def getPotencia(self) -> int:
        return self._potencia
class Notebook:
    def __init__(self):
        self._ligado = False
        self._bateria = None
        self._carregador = None
        self._tempo_ligado = 0
    def ligar(self) -> None:
        if (self._bateria is not None and self._bateria.getCarga() > 0) or self._carregador is not None:
            self._ligado = True
            print("notebook ligado")
        else:
            print("fail: não foi possível ligar")
    def desligar(self) -> None:
        if self._ligado:
            self._ligado = False
            print("notebook desligado")
        else:
            print("ja esta desligado")
    def usar(self, minutos: int) -> None:
        if not self._ligado:
            print("fail: desligado")
            return
        if self._bateria is None:
            self._tempo_ligado += minutos
            print(f"Notebook utilizado com sucesso")
            return
        if self._carregador is None:
            usado = self._bateria.consumir(minutos)
            self._tempo_ligado += usado
            if usado < minutos:
                self._ligado = False
                self._bateria.consumir(self._bateria.getCarga())
                print("fail: descarregou")

            else:
                print(f"Notebook utilizado com sucesso")
        else:
            potencia = self._carregador.getPotencia()
            self._bateria.carregar(minutos, potencia)
            self._tempo_ligado += minutos
            print(f"Notebook utilizado com sucesso")
    def setBateria(self,capacidade : int) -> None:
        self._bateria = Bateria(capacidade)
    def rmBateria(self) -> None:
        if self._bateria is None:
            print("fail: Sem bateria")
            return
        print(f"Removido {self._bateria.getCarga()}/{self._bateria.getcapacidade()}")
        self._bateria = None
    def setCarregador(self,potencia: int) -> None:
        if self._carregador is not None:
            print("fail: carregador ja conectado")
            return
        self._carregador = Carregador(potencia)
    def rmCarregador(self) -> None:
        if self._carregador is None:
            print("fail: sem carregador")
            return
        print(f"Removido {self._carregador.getPotencia()}W")
        self._carregador = None
    def mostrar(self) -> None:
        partes = [f"Notebook: {'ligado' if self._ligado else 'desligado'}"]
        if self._ligado:
            partes[0] += f" por {self._tempo_ligado} min"
        if self._carregador is not None:
            partes.append(f"Carregador {self._carregador.getPotencia()}W")
        if self._bateria is not None:
            partes.append(f"Bateria {self._bateria.getCarga()}/{self._bateria.getcapacidade()}")
        print(", ". join(partes))
def main() :
    notebook = Notebook()
    while True:
        try:
            line = input()
        except EOFError:
            break
        print("$" + line)
        line_norm = line.strip()
        if line_norm.startswith("$"):
            line_norm = line_norm[1:].strip()
        args = line_norm.split()
        if not args:
            continue
        cmd = args[0].lower()
        if cmd == "end":
            break
        elif cmd in ("show", "mostrar"):
            notebook.mostrar()
        elif cmd in ("ligar"):
            notebook.ligar()
        elif cmd in ("turn_off", "desligar"):
            notebook.desligar()
        elif cmd in ("use", "usar"):
            if len(args) < 2:
                print("uso: use <minutos>")
                continue
            try:
                minutos = int(args[1])
            except ValueError:
                print("minutos deve ser inteiro")
                continue
            notebook.usar(minutos)
        elif cmd =="set_battery":
            if len(args) < 2:
                print("uso: set battery <capacidade>")
                continue
            try:
                cap = int(args[1])
            except ValueError:
                print("capacidade deve ser inteiro")
                continue
            notebook.setBateria(cap)
        elif cmd == "rm_battery":
            notebook.rmBateria()
        elif cmd == "set_charger":
            if len(args)  < 2:
                print("uso: set_charger <potencia>")
                continue
            try:
                pot = int(args[1])
            except ValueError:
                print("potencia deve ser inteiro")
                continue
            notebook.setCarregador(pot)
        elif cmd == "rm_charger":
            notebook.rmCarregador()
        else:
            print("comando desconhecido")
if __name__=="__main__":
    main()