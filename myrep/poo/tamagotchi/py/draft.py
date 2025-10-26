class Pet:
    def __init__(self, energy: int, clean: int):
        self._energyMax = energy
        self._cleanMax = clean
        self._energy = energy
        self._clean = clean
        self._age = 0
        self._alive = True
class Game:
    def __init__(self, pet):
        self._pet = pet
    def show(self):
        p = self._pet
        print(f"E:{p._energy}/{p._energyMax}, L:{p._clean}/{p._cleanMax}, I:{p._age}")
def main():
    game = None
    primeira_linha = True
    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            continue
        if primeira_linha:
            print(line)
            primeira_linha = False
        parts = line.replace("·", " ").split()
        cmd = parts[0].lstrip("$").lower()
        if cmd == "init" and len(parts) >= 3:
            energy = int(parts[1])
            clean = int(parts[2])
            pet = Pet(energy, clean)
            game = Game(pet)
        elif cmd == "show":
            if game is not None:
                game.show()
        elif cmd == "end":
            break
if __name__ == "__main__":
    main()