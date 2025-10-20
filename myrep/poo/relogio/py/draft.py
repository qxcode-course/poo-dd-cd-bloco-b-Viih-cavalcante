class Watch :
    def __init__(self, hora: int, minuto: int, segundo: int) -> None:
        self._hora :int = hora
        self._minuto :int = minuto
        self._segundo :int = segundo

    def mostrar(self) -> None:
        print(self)


    def __str__(self)-> str:
        return f"{self._hora:02d}:{self._minuto:02d}:{self._minuto:02d}"
    def set(self, hora: int, minuto: int, segundo: int) -> None:
        if 0 <= hora <= 23:
            self._hora = hora
        else:
            print("fail: hora invalida")
        if 0 <= minuto <= 59:
            self._minuto = minuto
        else:
            print("fail: minuto invalido")
        if 0 <= segundo <= 59:
            self._segundo = segundo
        else:
            print("fail: segundo invalido")

def main():
    relogio = Watch (0, 0, 0)

    while True:
        line :str = input()
        print("$" + line)
        args : list [str] = line.split()
        cmd =  args[0]

        if cmd == "end" :
            break

        elif cmd == "show":
            relogio.mostrar()

        elif cmd == "set":
            hora = int(args[1])
            minuto = int(args[2])
            segundo = int(args[3])
            relogio.set(hora, minuto, segundo)


if __name__ == "__main__" :
    main()
