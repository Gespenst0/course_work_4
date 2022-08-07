from assets.arena import BaseSingleton
from assets.units import BaseUnit
from typing import Optional


class Arena(metaclass=BaseSingleton):
    """Класс арены"""
    STAMINA_RECOVERY_PER_TURN: float = 1
    player: Optional[BaseUnit] = None
    enemy: Optional[BaseUnit] = None
    game_on: bool = False
    battle_result: Optional[str] = None

    def start_game(self, player: BaseUnit, enemy: BaseUnit) -> None:
        """Старт игры"""
        self.player = player
        self.enemy = enemy
        self.game_on = True

    def player_attack(self):
        """Атака игрока"""
        player_result = self.player.attack(target=self.enemy)
        return player_result + " " + self.next_turn()

    def player_use_skill(self):
        """Использование абилки"""
        player_result = self.player.use_skill(target=self.enemy)
        return player_result + " " + self.next_turn()

    def next_turn(self):
        """Проверить хп игрока, восстановить выносливость и вызвать атаку противника"""
        if self._check_health():
            self._regenerate_stamina()
            enemy_result = self.enemy.attack(target=self.player)
            self._regenerate_stamina()
            return enemy_result
        return self.battle_result

    def _regenerate_stamina(self):
        """Регенерация выносливости"""
        player_stamina_recovery = self.STAMINA_RECOVERY_PER_TURN * self.player.unit_class.stamina_modifier
        enemy_stamina_recovery = self.STAMINA_RECOVERY_PER_TURN * self.enemy.unit_class.stamina_modifier
        self.player.stamina_points_ += round(player_stamina_recovery, 1)
        self.enemy.stamina_points_ += round(enemy_stamina_recovery, 1)

        if self.player.stamina_points_ > self.player.unit_class.max_stamina:
            self.player.stamina_points_ = self.player.unit_class.max_stamina
        if self.enemy.stamina_points_ > self.enemy.unit_class.max_stamina:
            self.enemy.stamina_points_ = self.enemy.unit_class.max_stamina

        print(f'Игрок восстановлено выносливости: {player_stamina_recovery}')
        print(f'Враг восстановлено выносливости: {player_stamina_recovery}')

    def _check_health(self):
        """Check if players have health left"""
        print(f'Здоровье игрока: {self.player.health_points_}')
        print(f'Здоровье врага: {self.enemy.health_points_}')

        if self.player.health_points_ > 0 and self.enemy.health_points_ > 0:
            return True

        if self.player.health_points_ <= 0 <= self.enemy.health_points_:
            self.battle_result = f'{self.player.name} проиграл {self.enemy.name}'

        if self.player.health_points_ >= 0 >= self.enemy.health_points_:
            self.battle_result = f'{self.player.name} победил {self.enemy.name}'

        if self.player.health_points_ <= 0 and self.enemy.health_points_ <= 0:
            self.battle_result = f'Ничья между {self.player.name} и {self.enemy.name}!'

        self._finish_game()

    def _finish_game(self):
        """Конец игры"""
        self._instances = {}
        self.game_on = False
