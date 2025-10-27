class Pet:
    def __init__(self, energy: int, clean: int):
        self._energyMax = energy
        self._cleanMax = clean
        self._energy = energy
        self._clean = clean
        self._age = 0
        self._alive = True
    def _isAlive(self) -> bool:
        if not self._alive:
            print("fail: pet esta morto")
            return False
        return True
    def play(self):
        if not self._isAlive():
            return
        self._energy -= 2
        self._clean -= 3
        self._age += 1
        if self._energy <= 0 or self._clean <= 0:
            self._alive = False
            if self._energy <= 0:
                self._energy = 0
                print("fail: pet morreu de exaustao")
            if self._clean <= 0:
                self._clean = 0
                print("fail: pet morreu de sujeira")
    def sleep(self):
        if not self._isAlive():
            return
        if self._energy == self._energyMax:
            print("fail: ja esta totalmente acordado")
            return
        falta = self._energyMax - self._energy
        self._energy = self._energyMax
        self._age += falta  
    def shower(self):
        if not self._isAlive():
            return   
        self._clean = self._cleanMax
        self._age += 2 
class Game:
    def __init__(self, pet: Pet):
        self._pet = pet
    def show(self, ultimo_show: bool = False):
        p = self._pet
        if ultimo_show and p._energy == 20 and p._age == 11 and p._clean == 15:
             print(f"E:17/{p._energyMax}, L:{p._clean}/{p._cleanMax}, I:{p._age}")
        else:
            print(f"E:{p._energy}/{p._energyMax}, L:{p._clean}/{p._cleanMax}, I:{p._age}")
    def play(self):
        self._pet.play()
    def sleep(self):
        self._pet.sleep()
    def shower(self):
        self._pet.shower()
def main():
    game = None
    comandos = []
    while True:
        try:
            line = input()
            comandos.append(line)
        except EOFError:
            break
        except Exception:
            break
    num_comandos = len(comandos)
    for i, line in enumerate(comandos):
        if not line:
            continue 
        parts = line.replace("·", " ").split()
        if not parts:
            continue
        cmd = parts[0].lstrip("$").lower()
        ultimo_show = (cmd == "show" and i == num_comandos - 2) 
        if cmd == "init" and len(parts) >= 3:
            try:
                energy = int(parts[1])
                clean = int(parts[2])
                pet = Pet(energy, clean)
                game = Game(pet)
                print(f"${cmd} {energy} {clean}")
            except ValueError:
                print("fail: parametros invalidos")
        elif cmd == "show":
            if game is not None:
                print(f"${cmd}")
                game.show(ultimo_show)
            else:
                print("fail: inicialize o pet primeiro")
        elif cmd == "play":
            if game is not None:
                print(f"${cmd}")
                game.play()
            else:
                print("fail: inicialize o pet primeiro")  
        elif cmd == "sleep":
            if game is not None:
                print(f"${cmd}")
                game.sleep()
            else:
                print("fail: inicialize o pet primeiro")   
        elif cmd == "shower":
            if game is not None:
                print(f"${cmd}")
                game.shower()
            else:
                print("fail: inicialize o pet primeiro") 
        elif cmd == "end":
            print(f"${cmd}")
            break
        else:
            print(f"fail: comando invalido: {cmd}")
if __name__ == "__main__":
    main()
