class pessoa:
    def __init__(self) -> None:
        self._name :str = name
        self._age :int = age


class motoca:
    def __init__(self, potencia :int = 1) -> None:
        self.potencia : int = potencia
        self.time : int = 0
        self.pessoa = None

    def toString(self) -> str:
        if self.pessoa is None:
            person_str = "empty"
        else:
            person_str = f"{self.pessoa.get.Name()}:{self.pessoa.get.Age()}"
            return f"power: {self.potencia}, time :{self.time}, person :({person_str})"
    def __str__(self)-> str:
        return self.toString()   





def main():
     moto = motoca()
     while true:
         try:
             line = input().strip()
         except EOFERROR:
             break
         if line == "":
             continue
         if not line.startswith("$"):
             continue
         parts =line.split()
         cmd = parts{0}
         if cmd == "$end":
             break
         elif cmd == "$show":
             print(moto.toString())
         else:
             print("fail :unknown command")
if __name__ == "__ main__":
    main()