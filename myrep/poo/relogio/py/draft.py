class Watch :
    def __init__(self, hora: int, minuto: int, segundo: int):
        self._hora :int = hora
        self._minuto :int = minuto
        self._segundo :int = segundo

    def mostrar(self) -> None:
        print(self)


    def __str__(self)-> str:
        return f"{self._hora:02d}:{self._minuto:02d}:{self._segundo:02d}"
def main():
    relogio = Watch (0, 0, 0)
    while True:
        line :str = input()
        print("$" + line)
        args : list [str] = line.split(" ")
        cmd =  args[0]
        if cmd == "end" :
            break
        elif cmd == "show":
            relogio.mostrar()

if __name__ == "__main__" :
    main()
