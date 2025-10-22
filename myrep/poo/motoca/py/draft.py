class pessoa:
    def __init__(self) -> None:
        self._name :str = name
        self._age :int = age

    def getName(self) -> str:
        return self._name
    
    def getAge(self) -> int:
        return self._age

    def toString(self) -> str:
        return f"{self._name}:{self._age}"
    
    def __str__(self) -> str:
        return self.toString()
    
class motoca:
    def __init__(self, potencia :int = 1) -> None:
        self.potencia : int = potencia
        self.time : int = 0
        self.pessoa = None

    def inserir(self, pessoa: pessoa) -> bool :
        if self.pessoa is not None :
            print("fail: busy motorcycle")
            return False
        self.pessoa = pessoa
        return True
    
    def remover(self) -> pessoa | None:
        if self.pessoa is None:
            print("fail: empty motocycle")
            return None
        p = self.pessoa
        self.pessoa = None
        print(p.toString())
        return p
    
    def buyTime(self, minuto: int) -> None:
        self.time += minutos

    def drive(self, minutos :int) -> None:
              self.time <=0:
              print("fail: buy time firt")
              return

    def drive(self, minutos :int) -> None:
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
     while True:
         try:
             line = input().strip()
         except EOFError:
             break
         if line == "":
             continue
         if not line.startswith("$"):
             continue
         parts =line.split()
         cmd = parts[0]

         if cmd == "$end":
            break
         elif cmd == "$show":
            print(moto.toString())
         else:
            print("fail: unknown command")


if __name__ == "__main__":
    main()