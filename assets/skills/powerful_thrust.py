from assets.skills import BaseSkill


class PowerfulThrust(BaseSkill):
    """Скил мощный укол"""
    name: str = 'Мощный укол'
    damage: float = 15.0
    stamina_required: float = 5.0

    def _skill_effect(self):
        self.target.health_points_ -= self.damage
        self.user.stamina_points_ -= self.stamina_required
        return f'{self.user.name} использует {self.user.unit_class.skill.name} и наносит {self.damage} урона сопернику.'
