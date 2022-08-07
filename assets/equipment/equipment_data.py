from dataclasses import dataclass, field


@dataclass
class EquipmentData:
    weapons: list = field(default_factory=list)
    armor: list = field(default_factory=list)
