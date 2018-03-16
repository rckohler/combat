import random
from C_Ability import Ability
from helpers import *
class Guy:
    PUNCH = Ability("PUNCH",-2,1,1,Ability.ATTACKING)
    BLOCK = Ability("BLOCK",-5,0,4,Ability.BLOCKING,None,None,None,Ability.ATTACKING)
    GRAPPLE = Ability ("GRAPPLE",-5,0,2,Ability.GRAPPLED,None,Ability.GRAPPLED,None,Ability.BLOCKING)
    JUDO_THROW = Ability("JUDO_THROW",-5, 0, 2,None,Ability.GRAPPLED,Ability.PRONE,Ability.GRAPPLED,Ability.GRAPPLED)

    def __init__(self):
        names = ["Abe","Bob","Carl","Doug","Edward","Franklin","Greg","Hans","Igor","Jayce","Kelvin","Lamb","Mo","Ned","Owen","Paul","Quinn","Ryan","Sal","Tommy","Ulysses","Victor","Wes","Xavier","Yvenn","Zed"]
        self.name = random.choice(names) + " " + random.choice(names) + "son"
        self.advantage = 0
        self.statusEffects = []
        self.moves = [Guy.PUNCH, Guy.BLOCK, Guy.GRAPPLE, Guy.JUDO_THROW]
        self.isDead = False
    def selectTarget(self,guys):
        target = getChoiceFromListOfNamedItems(self.name + " choose your target.", guys)
        return target
    def selectAttack(self):
        attack = getChoiceFromListOfNamedItems(self.name + " choose your attack.",self.moves)
        return attack

    def handleIncomingDamage(self,attacker,damage):
        if damage > 0:
            print(attacker.name + " smacked "+ self.name + ".")
            self.advantage -= random.randint(1,6)
            if self.advantage < 5 and random.randint(1,5)== 3:
                print (attacker.name + " killed " + self.name + ".")
                self.isDead = True
        #more will be added here eventually.

    def debugOutput(self):
        statusEffectString = ""

        for s in self.statusEffects:
            if s == 0:
                statusEffectString+= " Grappled "
            if s == 1:
                statusEffectString += " Prone "
            if s == 2:
                statusEffectString += " Blocking "
            if s == 3:
                statusEffectString += " Attacking "

        print(self.name +":" + statusEffectString + " " + str(self.advantage))
    def addStatusEffect(self,status):
        if not self.statusEffects.__contains__(status):
            self.statusEffects.append(status)
    def removeStatusEffect(self,status):
        if self.statusEffects.__contains__(status):
            self.statusEffects.remove(status)
class AI_Guy(Guy):
    def __init__(self):
        super().__init__()
    def selectAttack(self):
        return random.choice(self.moves)
    def selectTarget(self,possibleTargets):
        while 1:
            target = random.choice(possibleTargets)
            if not target == self:
                return target
