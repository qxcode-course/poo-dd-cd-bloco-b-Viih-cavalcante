class Camisa:
    def __init__(self) -> None :
        self._tamanho :str = ""
    def getTamanho(self) -> str:
        return self._tamanho
    def setTamanho(self, valor: str):
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        valor = valor.strip().upper()
        if valor == "end":
            return None
        if valor in tamanhos_validos:
            self.__tamanho = valor
        else:
            print(" Tamanho inválido!")
            print("Tamanhos válidos são:", ", ".join(tamanhos_validos))
def main():
    camisa = Camisa()
    print("tamanhos validos: PP, P, M, G, GG, XG")
    print('digite "end" para encerrar o pragrama,')
    while True:
        tamanho = input("digite seu tamanho de roupa: ")resultado = camisa.setTamanho(tamanho
        if ok:
            break
    print("parabens, voce comprou uma blusa tamanho", camisa.getTamanho())
if __name__=="__main__":
    main()
