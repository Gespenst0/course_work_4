from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from assets.units import BaseUnit


class BaseSkill(ABC):
    """Базоввый класс для абилок"""
    name: Optional[str] = None
    damage: float = 0
    stamina_required: float = 0
    user = None
    target = None

    @abstractmethod
    def _skill_effect(self):
        pass

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        """Использовать абилку, если достаточно выносливости"""
        self.user = user
        self.target = target

        if self.user.stamina_points_ < self.stamina_required:
            return (f"{self.user.name} попытался использовать {self.user.unit_class.skill.name}, "
                    f"но у него не хватило выносливости.")
        return self._skill_effect()
