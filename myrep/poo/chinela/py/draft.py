class Chinela:
    def __init__(self):
        self._tamanho = 0

    def setTamanho(self, tamanho: int):
        if tamanho < 20 or tamanho > 50:
            print("fail: tamanho fora do intervalo permitido (20-50)")
            return False
        if tamanho % 2 != 0:
            print("fail: tamanho deve ser par")
            return False
        self._tamanho = tamanho
        return True

    def getTamanho(self):
        return self._tamanho


def main():
    chinela = Chinela()
    while True:
        try:
            valor = int(input("Digite o tamanho da chinela: "))
            if chinela.setTamanho(valor):
                break
        except ValueError:
            print("fail: entrada invalida, digite um numero inteiro")

    print(f"Tamanho da chinela definido: {chinela.getTamanho()}")


if __name__ == "__main__":
    main()