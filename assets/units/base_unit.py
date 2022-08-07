from __future__ import annotations
from abc import ABC

from assets.equipment import Armor, Weapon
from assets.classes import UnitClass


class BaseUnit(ABC):

    def __init__(self, name: str, unit_class: UnitClass, weapon: Weapon, armor: Armor):
        self.name = name
        self.unit_class = unit_class
        self.health_points_: float = unit_class.max_health
        self.stamina_points_: float = unit_class.max_stamina
        self.weapon = weapon
        self.armor = armor
        self.skill_used: bool = False
        
    @property
    def health_points(self):
        if self.health_points_ < 0:
            return 0
        return round(self.health_points_, 1)

    @property
    def stamina_points(self):
        return round(self.stamina_points_, 1)

    def attack(self, target: BaseUnit) -> str:
        if self.stamina_points_ >= self.weapon.stamina_per_hit:

            # Просчитать нанесенный дамаг цели
            damage_inflicted = self._calculate_damage(target)
            target._get_damage(damage_inflicted)

            # Обновить очки выносливости
            self.stamina_points_ -= self.weapon.stamina_per_hit
            target.stamina_points_ -= target.armor.stamina_per_turn

            # Выносливость не может опуститься ниже нуля
            if target.stamina_points_ < 0:
                target.stamina_points_ = 0

            print(f'{self.name} потрачено выносливости: {self.weapon.stamina_per_hit}')
            print(f'{target.name} потрачено выносливости: {target.armor.stamina_per_turn}')

            if damage_inflicted > 0:
                return (f"{self.name}, используя {self.weapon.name}, "
                        f"пробивает {target.armor.name} соперника и наносит {damage_inflicted} урона.")
            return (f"{self.name}, используя {self.weapon.name}, "
                    f"наносит удар, но {target.armor.name} соперника его останавливает.")

        return (f"{self.name} попытался использовать {self.weapon.name}, "
                f"но у него не хватило выносливости.")

    def use_skill(self, target: BaseUnit):
        """Использование абилки"""
        if self.skill_used:
            return (f"{self.name} попытался использовать {self.unit_class.skill.name}, "
                    f"но у него не хватило выносливости.")
        self.skill_used = True
        return self.unit_class.skill.use(user=self, target=target)

    def _calculate_damage(self, target: BaseUnit) -> float:
        """Подсчет урона"""
        damage = self.weapon.calculate_damage() * self.unit_class.attack_modifier
        defence = target.armor.defence if target.stamina_points_ >= target.armor.stamina_per_turn else 0

        if damage <= defence:
            damage_inflicted = 0
        else:
            damage_inflicted = damage - defence

        print(f'{self.name} урон от оружия: {damage}')
        print(f'{target.name} защита: {defence}')
        print(f'{target.name} получает урон: {damage_inflicted}')
        return round(damage_inflicted, 1)

    def _get_damage(self, damage_inflicted: float) -> None:
        """Уменьшить хп на величину полученного урона"""
        self.health_points_ -= damage_inflicted

