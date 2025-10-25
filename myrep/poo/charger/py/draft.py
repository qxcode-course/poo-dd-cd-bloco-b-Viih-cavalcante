class Notebook:
    def __init__(self):
        self._ligado: bool = False
        self._bateria = None
        self._carregador = None

    def getLigado(self) -> bool:
        return self._ligado

    def setLigado(self, valor: bool) -> None:
        self._ligado = valor

    def ligar(self) -> None:
        if self._bateria is None and self._carregador is None:
            print("fail: não foi possível ligar")
        else:
            self._ligado = True
            print("notebook ligado")

    def desligar(self) -> None:
        if self._ligado:
            self._ligado = False
            print("notebook desligado")
        else:
            print("já está desligado")

    def mostrar(self) -> None:
        status = "ligado" if self._ligado else "desligado"
        print(f"Notebook: {status}")

    def usar(self, tempo: int) -> None:
        if not self._ligado:
            print("erro: ligue o notebook primeiro")
            return
        print(f"Usando por {tempo} minutos")


def main():
    notebook = Notebook()
    while True:
        try:
            line: str = input()
        except EOFError:
            break
        print("$" + line)
        line_norm = line.strip()
        if line_norm.startswith("$"):
            line_norm = line_norm[1:].lstrip()
        args = line_norm.split()
        if len(args) == 0:
            continue
        cmd = args[0].lower()
        if cmd == "end":
            break
        elif cmd == "show" or cmd == "mostrar":
            notebook.mostrar()
        elif cmd == "ligar":
            notebook.ligar()
        elif cmd == "desligar":
            notebook.desligar()
        elif cmd == "usar":
            if len(args) < 2:
                print("uso: usar <minutos>")
                continue
            try:
                minutos = int(args[1])
            except ValueError:
                print("minutos deve ser um número inteiro")
                continue
            notebook.usar(minutos)
        else:
            print("comando desconhecido")
if __name__ == "__main__":
    main()