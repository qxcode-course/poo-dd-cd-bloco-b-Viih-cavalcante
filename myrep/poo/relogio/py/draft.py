class Watch :
    def __init__(self, hora: int, minuto: int, segundo: int) -> None:
        self._hora :int = hora
        self._minuto :int = minuto
        self._segundo :int = segundo

    def mostrar(self) -> None:
        print(self)


    def __str__(self)-> str:
        return f"{self._hora:02d}:{self._minuto:02d}:{self._segundo:02d}"
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
    def nextSecond(self) -> None :
      self._segundo +=1
      if  self._segundo == 60:
        self._segundo = 0
        self._minuto += 1
      if self._minuto == 60:
          self._minuto = 0
          self._hora += 1
      if self._hora == 24:
          self._hora = 0
def main():
    relogio = Watch (0, 0, 0)

    while True:
        try:
            raw_line: str = input()
        except EOFError:
            break
        print("$" + raw_line)

        line = raw_line.strip()
        if line == "":
            continue

        args : list [str] = line.split()
        cmd =  args[0]

        if cmd == "end" :
            break

        elif cmd == "show":
            relogio.mostrar()

        elif cmd == "set":
            if len(args) < 4:
                continue
            try:
             hora = int(args[1])
             minuto = int(args[2])
             segundo = int(args[3])
            except ValueError :
                continue
            relogio.set(hora, minuto, segundo)
        elif cmd == "next":
            relogio.nextSecond()
        elif cmd == "init":
            relogio = Watch(0, 0, 0)
            if len(args) < 4:
                continue
            try:
                h = int(args[1]); m = int(args[2]); s = int(args[3])
            except ValueError:
                continue
            relogio.set(h, m, s)

if __name__ == "__main__" :
    main()
