class Roupa:
    def __init__(self) -> None:
        self._tamanho: str = ""  # começa vazio

    def getTamanho(self) -> str:
        return self._tamanho
    def setTamanho(self, tamanho: str) -> None:
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if tamanho in tamanhos_validos:
            self._tamanho = tamanho
        else:
            print(f"Erro: tamanho inválido! Os tamanhos permitidos são: {', '.join(tamanhos_validos)}")
def main():
    roupa = Roupa()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split()
        
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(f"size: ({roupa.getTamanho()})")
        elif args[0] == "size" and len(args) > 1:
            roupa.setTamanho(args[1])
main()

