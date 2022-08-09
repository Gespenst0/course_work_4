from abc import ABC
from dataclasses import dataclass

from assets.skills import BaseSkill


@dataclass
class UnitClass(ABC):
    """Дата класс для юнита"""
    name: str
    max_health: float
    max_stamina: float
    attack_modifier: float
    stamina_modifier: float
    armor_modifier: float
    skill: BaseSkill