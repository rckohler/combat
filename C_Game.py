from Units import *
from C_CombatEncounter import  CombatEncounter

class Game:
    def __init__(self):
        self.units = []
        for i in range(2):
            self.units.append(AI_Guy())
        self.units.append(Guy())

    def runGame(self):
        c = CombatEncounter(self.units)
        while 1:
            c.run()
            for u in self.units:
                u.debugOutput()
g = Game()
g.runGame()