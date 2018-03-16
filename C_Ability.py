class Ability:
    GRAPPLED = 0
    PRONE = 1
    BLOCKING = 2
    ATTACKING = 3
    def __init__(self,name, type, advantageRequirement, damage, advantageEffect, statusAddedMe = None, statusRemovedMe = None, statusAddedToThem = None, statusRemovedThem = None, condition = None):
        self.type = type
        self.name = name
        self.advantageRequirement = advantageRequirement
        self.damage = damage
        self.statusRemovedMe = statusRemovedMe
        self.statusRemovedThem = statusRemovedThem
        self.advantageEffect = advantageEffect
        self.condition = condition
        self.statusAddedMe = statusAddedMe
        self.statusAddedThem = statusAddedToThem
        self.currentChoice = 0

    def enact(self,actor,victim):
        #advantage
        victim.advantage -= self.advantageEffect
        actor.advantage += self.advantageEffect
        #statuses
        actor.addStatusEffect(self.statusAddedMe)
        actor.removeStatusEffect(self.statusRemovedMe)
        victim.addStatusEffect(self.statusAddedThem)
        victim.removeStatusEffect(self.statusRemovedThem)
        #damage
        victim.handleIncomingDamage(actor,self.damage)