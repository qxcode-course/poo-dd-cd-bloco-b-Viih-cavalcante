class Pessoa:
    def __init__(self, name: str, age: int) -> None:
        self.__name: str = name
        self.__age: int = age

    def getName(self) -> str:
        return self.__name

    def getAge(self) -> int:
        return self.__age

    def toString(self) -> str:
        return f"{self.__name}:{self.__age}"

    def __str__(self) -> str:
        return self.toString()


class Motoca:
    def __init__(self, potencia: int = 1) -> None:
        self.potencia: int = potencia
        self.time: int = 0
        self.pessoa: Pessoa | None = None

    def init(self, potencia: int = 1) -> None:
        self.potencia = potencia
        self.time = 0
        self.pessoa = None

    def inserir(self, pessoa: Pessoa) -> bool:
        if self.pessoa is not None:
            print("fail: busy motorcycle")
            return False
        self.pessoa = pessoa
        return True

    def remover(self) -> Pessoa | None:
        if self.pessoa is None:
            print("fail: empty motorcycle")
            return None
        p = self.pessoa
        self.pessoa = None
        print(p.toString())
        return p

    def buyTime(self, minutos: int) -> None:
        self.time += minutos

    def drive(self, minutos: int) -> None:
        if self.time <= 0:
            print("fail: buy time first")
            return

        if self.pessoa is None:
            print("fail: empty motorcycle")
            return

        if self.pessoa.getAge() > 10:
            print("fail: too old to drive")
            return

        new_time = self.time - minutos
        if new_time <= 0:
            print(f"fail: time finished after {self.time} minutes")
            self.time = 0
        else:
            self.time = new_time

    def honk(self) -> str:
        return "P" + ("e" * self.potencia) + "m"

    def toString(self) -> str:
        if self.pessoa is None:
            person_str = "empty"
        else:
            person_str = f"{self.pessoa.getName()}:{self.pessoa.getAge()}"
        return f"power:{self.potencia}, time:{self.time}, person:({person_str})"

    def __str__(self) -> str:
        return self.toString()


def main():
    moto = Motoca()

    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        if line == "":
            continue

        # transforma comandos sem $ em comandos com $
        if not line.startswith("$"):
            line = "$" + line

        print(line)  # <<< imprime o comando antes da resposta

        parts = line.split()
        cmd = parts[0]

        if cmd == "$end":
            break

        elif cmd == "$show":
            print(moto.toString())

        elif cmd == "$init":
            if len(parts) >= 2:
                try:
                    p = int(parts[1])
                except ValueError:
                    p = 1
                moto.init(p)
            else:
                moto.init(1)

        elif cmd == "$enter":
            if len(parts) < 3:
                print("fail: invalid arguments")
                continue
            nome = parts[1]
            try:
                idade = int(parts[2])
            except ValueError:
                print("fail: invalid age")
                continue
            pessoa_obj = Pessoa(nome, idade)
            moto.inserir(pessoa_obj)

        elif cmd == "$leave":
            moto.remover()

        elif cmd == "$buy":
            if len(parts) < 2:
                print("fail: invalid arguments")
                continue
            try:
                minutos = int(parts[1])
            except ValueError:
                print("fail: invalid time")
                continue
            moto.buyTime(minutos)

        elif cmd == "$drive":
            if len(parts) < 2:
                print("fail: invalid arguments")
                continue
            try:
                minutos = int(parts[1])
            except ValueError:
                print("fail: invalid time")
                continue
            moto.drive(minutos)

        elif cmd == "$honk":
            print(moto.honk())

        else:
            print("fail: unknown command")


if __name__ == "__main__":
    main()