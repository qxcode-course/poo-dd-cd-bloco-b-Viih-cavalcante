import sys, io, os

sys.stdout = io.TextIOWrapper(os.fdopen(sys.stdout.fileno(), "wb"), encoding="utf-8")
class Bateria:
    def __init__(self, capacidade: int):
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

    def carregar(self, minutos: int, potencia: int) -> None:
        self._carga = min(self._capacidade, self._carga + minutos * potencia)

    def adicionar_carga(self, quantidade: int) -> None:
        self._carga = min(self._capacidade, self._carga + quantidade)

class Carregador:
    def __init__(self, potencia: int):
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
        if (self._bateria and self._bateria.getCarga() > 0) or self._carregador:
            self._ligado = True
        else:
            print("fail: não foi possível ligar")

    def desligar(self) -> None:
        if self._ligado:
            self._ligado = False
        else:
            print("já esta desligado")

    def usar(self, minutos: int) -> None:
        if not self._ligado:
            print("fail: desligado")
            return
        if not self._bateria and not self._carregador:
            print("fail: sem energia")
            self._ligado = False
            return
        if self._bateria is None and self._carregador:
            self._tempo_ligado += minutos
            return
        if self._carregador is None and self._bateria:
            usado = self._bateria.consumir(minutos)
            self._tempo_ligado += usado
            if self._bateria.getCarga() == 0:
                self._ligado = False
                print("fail: descarregou")
            return
        if self._bateria and self._carregador:
            for _ in range(minutos):
                usado = self._bateria.consumir(1)
                self._bateria.adicionar_carga(self._carregador.getPotencia())
                self._tempo_ligado += 1
                if usado == 0:
                    self._ligado = False
                    print("fail: descarregou")
                    break

    def setBateria(self, capacidade: int) -> None:
        self._bateria = Bateria(capacidade)

    def rmBateria(self) -> None:
        if not self._bateria:
            print("fail: Sem bateria")
            return
        print(f"Removido {self._bateria.getCarga()}/{self._bateria.getcapacidade()}")
        self._bateria = None
        if not self._carregador:
            self._ligado = False

    def setCarregador(self, potencia: int) -> None:
        if self._carregador:
            print("fail: carregador já conectado")
            return
        self._carregador = Carregador(potencia)

    def rmCarregador(self) -> None:
        if not self._carregador:
            print("fail: Sem carregador")
            return
        print(f"Removido {self._carregador.getPotencia()}W")
        self._carregador = None
        if not self._bateria:
            self._ligado = False

    def mostrar(self) -> None:
        partes = [f"Notebook: {'ligado' if self._ligado else 'desligado'} por {self._tempo_ligado} min"] if self._ligado else ["Notebook: desligado"]
        if self._carregador:
            partes.append(f"Carregador {self._carregador.getPotencia()}W")
        if self._bateria:
            partes.append(f"Bateria {self._bateria.getCarga()}/{self._bateria.getcapacidade()}")
        print(", ".join(partes))

def main():
    notebook = Notebook()
    while True:
        try:
            line = input()
        except EOFError:
            break
        print("$" + line)
        args = line.strip().lstrip("$").split()
        if not args:
            continue
        cmd = args[0].lower()
        if cmd == "end":
            break
        elif cmd in ("show", "mostrar"):
            notebook.mostrar()
        elif cmd in ("turn_on", "ligar"):
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
        elif cmd == "set_battery":
            if len(args) < 2:
                print("uso: set_battery <capacidade>")
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
            if len(args) < 2:
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

if __name__ == "__main__":
    main()