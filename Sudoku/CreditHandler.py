from random import randrange
from Error.InvalidCreditsException import InvalidCreditsException

class CreditHandler:
    def __init__(self, credits, diff_lvl):
        self.diff_lvl = diff_lvl
        self.credits = credits
        self.cooldown = self.reset_cooldown()

    def get_credits(self):
        return self.credits
    
    def spend(self, amount):
        if amount > self.credits:
            raise InvalidCreditsException("\n❌ Insufficient credits!")
        self.credits -= amount

    def bonus(self):
        if self.cooldown == 0:
            self.reset_cooldown()
            return self.give_bonus()
        self.cooldown -= 1
        return 0
    
    def reset_cooldown(self):
        self.cooldown = randrange(1, (self.diff_lvl * 2) + 1)
        return self.cooldown

    def give_bonus(self):
        bonus = randrange(1,4)
        self.credits += bonus
        print(f'\n + {bonus} BONUS CREDITS 🪙')
        return bonus