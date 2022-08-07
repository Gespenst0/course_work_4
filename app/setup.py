from assets.arena.arena import Arena
from assets.classes import UnitClass
from assets.equipment import Equipment
from assets.skills import PowerfulThrust, FerociousKick
from app.config import BaseConfig

equipment = Equipment(BaseConfig.EQUIPMENT_PATH)

heroes = {
    'player': None,
    'enemy': None
}
arena = Arena()


WarriorClass = UnitClass(
    name='Воин',
    max_health=50.0,
    max_stamina=25.0,
    attack_modifier=1.5,
    stamina_modifier=1.2,
    armor_modifier=1.0,
    skill=PowerfulThrust()
)

ThiefClass = UnitClass(
    name='Вор',
    max_health=60.0,
    max_stamina=30.0,
    attack_modifier=0.8,
    stamina_modifier=0.9,
    armor_modifier=1.0,
    skill=FerociousKick()
)

unit_classes = {
    WarriorClass.name: WarriorClass,
    ThiefClass.name: ThiefClass
}
