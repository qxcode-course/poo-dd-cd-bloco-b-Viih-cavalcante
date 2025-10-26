import sys, io, os

sys.stdout = io.TextIOWrapper(os.fdopen(sys.stdout.fileno(), "wb"), encoding="utf-8")
class Roupa:
        def __init__(self):
            self.__tamanho: str = ""

        def getTamanho(self) -> str:
            return self.__tamanho
    
        def setTamanho(self, value: str):
            tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
            if value in tamanhos_validos:
                self.__tamanho = value
            else:
                print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")

        def __str__(self):
         return f"size: ({self.__tamanho})"

def main():
    roupa = Roupa()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split()

        if len(args) == 0:
            continue
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(roupa)
        elif args[0] == "size":
            if len(args) > 1:
                roupa.setTamanho(args[1])
            else:
                print("fail: informe o tamanho desejado")
        else:
            print("fail: comando desconhecido")

main()