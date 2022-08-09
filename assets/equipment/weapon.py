from dataclasses import dataclass
from random import uniform

import marshmallow
import marshmallow_dataclass


@dataclass
class Weapon:
    """Класс для оружия"""
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    class Meta:
        unknown = marshmallow.EXCLUDE

    def calculate_damage(self):
        """Просчитать нанесенный дамаг, основываясь на максимальном и минимальном значении"""
        return uniform(self.min_damage, self.max_damage)


WeaponSchema = marshmallow_dataclass.class_schema(Weapon)




