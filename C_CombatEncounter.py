from helpers import getChoiceFromListOfNamedItems
class CombatEncounter:
    def __init__(self,guys):
        self.guys = guys
    def run(self):
        self.handleUnitActions()
        self.removeTheDead()
    def handleUnitActions(self):
        proposedActions = []
        for guy in self.guys:

            proposedActions.append([guy.selectAttack(), guy, guy.selectTarget(self.guys)])

        for actionTargetTriad in proposedActions:
            action = actionTargetTriad[0]
            actor = actionTargetTriad[1]
            target = actionTargetTriad[2]
            if CombatEncounter.validateAttack(action, actor, target):
                print(actor.name + " elected to " + action.name + " " + target.name+".")
                action.enact(actor, target)
    def removeTheDead(self):
        dead = []
        for unit in self.guys:
            if unit.isDead:
                dead.append(unit)
        for unit in dead:
            self.guys.remove(unit)
    @staticmethod
    def validateAttack(attack, actor, target):
        move = attack
        if actor.advantage > move.advantageRequirement:
            if target.statusEffects.__contains__(move.condition):
                return True
            if move.condition == None:
                return True
        return False