from random import randint

from assets.units import BaseUnit


class Enemy(BaseUnit):

    def attack(self, target: BaseUnit) -> str:
        """Логика атаки противника
        Если абилка не была применена, то существует вероятность, что
        она применится при обысной атаке
        """

        if not self.skill_used:
            use_skill = randint(0, 9)
            if use_skill == 0:
                return self.use_skill(target)

        return super().attack(target)
