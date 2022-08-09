from assets.skills import BaseSkill


class FerociousKick(BaseSkill):
    """Скил пинка"""
    name: str = 'Свирепый пинок'
    damage: float = 12.0
    stamina_required: float = 6.0

    def _skill_effect(self) -> str:
        """Уменьшить хп врага и отнять стамину использовавшего скил"""
        self.target.health_points_ -= self.damage
        self.user.stamina_points_ -= self.stamina_required
        return f'{self.user.name} использует {self.user.unit_class.skill.name} и наносит {self.damage} урона сопернику.'
