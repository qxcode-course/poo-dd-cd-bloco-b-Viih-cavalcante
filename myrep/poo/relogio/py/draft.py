class Watch :
    def __init__(self) :
        self._hora :int = 0
        self._minuto :int = 0
        self._segundo :int = 0

    def mostrar(self) -> None:
        print(self)


    def __srt__(self):
        return f"{self._hora:2d}:{self._minuto:2d}:{self._segundo}"
def main():