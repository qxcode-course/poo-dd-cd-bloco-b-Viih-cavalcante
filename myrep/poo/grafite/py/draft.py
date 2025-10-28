class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness: float = thickness  #calibre
        self.__hardness: str = hardness      #dureza
        self.__size: int = size              #tamanho
    def getThickness(self) -> float:
        return self.__thickness
    def getHardness(self) -> str:
        return self.__hardness
    def getSize(self) -> int:
        return self.__size
    def setSize(self, size: int):
        self.__size = size
    def usagePerSheet(self) -> int:
        if self.__hardness == "HB":
            return 1
        if self.__hardness == "2B":
            return 2
        if self.__hardness == "4B":
            return 4
        if self.__hardness == "6B":
            return 6
        return 0
    def __str__(self) -> str:
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"
class Pencil:
    def __init__(self, thickness: float):
        self.__tip: None = None              #grafite atual (começa sem grafite)
        self.__thickness: float = thickness  #calibre
    def getTip(self) -> Lead | None:
        return self.__tip
    def getThickness(self) -> float:
        return self.__thickness
    def hasGrafite(self) -> bool:
        if self.__tip != None:
            return True
        else:
            return False
    def insert(self, grafite: Lead) -> bool:
        if self.hasGrafite(): #verifica se ja existe um grafite na lapiseira
            print("fail: ja existe grafite")
            return False
        elif grafite.getThickness() != self.__thickness:
            print("fail: calibre incompativel")
            return False
        self.__tip = grafite
        return True
    def remove(self) -> Lead | None:
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return None
        else:
            Aux: Lead = self.__tip
            self.__tip = None
            return Aux
    def writePage(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return
        grafite = self.__tip
        gasto = grafite.usagePerSheet()
        tamanho_atual = grafite.getSize()
        if tamanho_atual <= 10:
            print("fail: tamanho insuficiente")
            return 
        novo_tamanho = tamanho_atual - gasto
        if novo_tamanho < 10:
            grafite.setSize(10)
            print("fail: folha incompleta")
            return
        grafite.setSize(novo_tamanho)
    def __str__(self) -> str:
        if self.hasGrafite():
            return f"calibre: {self.__thickness}, grafite: {self.__tip}"
        else:
            return f"calibre: {self.__thickness}, grafite: null" 
def main():
    pencil: Pencil | None = None
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split()
        if args[0] == "show":
            if pencil != None:
                print(pencil)
            else:
                print("fail: lapiseira nao iniciada")
        elif args[0] == "end":
            break
        elif args[0] == "init":
            thickness = float(args[1])
            pencil = Pencil(thickness)
        elif args[0] == "insert":
            if pencil is None:
                print("fail: lapiseira nao iniciada")
                continue
            thickness = float(args[1])
            hardness = args[2]
            size = int(args[3])
            grafite = Lead(thickness, hardness, size)
            pencil.insert(grafite)
        elif args[0] == "remove":
            pencil.remove()
        elif args[0] == "write":
                  pencil.writePage()
main()
