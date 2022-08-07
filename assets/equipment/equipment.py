import json
from typing import List

from assets.equipment.armor import ArmorSchema, Armor
from assets.equipment.equipment_data import EquipmentData
from assets.equipment.weapon import WeaponSchema, Weapon


class Equipment:
    """Интерфейс для управлянию юнитом"""

    def __init__(self, filename: str):
        self.filename = filename
        self.equipment: EquipmentData = self._create_equipment()

    def _create_equipment(self) -> EquipmentData:
        """Создать экипировку из json файла"""
        with open(self.filename, encoding='utf-8') as file:
            data = json.load(file)

            return EquipmentData(
                    weapons=WeaponSchema(many=True).load(data['weapons']),
                    armor=ArmorSchema(many=True).load(data['armors']))

    def get_weapon(self, weapon_name: str):
        """Получить оружие по его названию"""
        for weapon in self.equipment.weapons:
            if weapon.name == weapon_name:
                return weapon

    def get_weapon_names(self) -> List[Weapon]:
        """Получить список всего оружия"""
        return [weapon.name for weapon in self.equipment.weapons]

    def get_armor(self, armor_name: str):
        """Получить броню по названию"""
        for armor in self.equipment.armor:
            if armor.name == armor_name:
                return armor

    def get_armor_names(self) -> List[Armor]:
        """Получить весь список брони"""
        return [armor.name for armor in self.equipment.armor]
