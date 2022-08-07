from flask import Blueprint, request, render_template, redirect, url_for

from assets.units import Player, Enemy
from app.setup import heroes, equipment, unit_classes


start_bp = Blueprint('Start', __name__)


@start_bp.route('/')
def start():
    """Главная страница"""
    return render_template('index.html')


@start_bp.route('/choose-hero/', methods=['GET', 'POST'])
def choose_hero():
    """Конфигурация юнита игрока"""

    if request.method == 'GET':
        result = {
            "header": 'Выбор героя для игрока',
            "classes": unit_classes,
            "weapons": equipment.get_weapon_names(),
            "armors": equipment.get_armor_names()
        }

        return render_template('hero_choosing.html', result=result)

    if request.method == 'POST':
        user_name = request.form.get('name')
        unit_class = unit_classes[request.form.get('unit_class')]
        weapon = equipment.get_weapon(request.form.get('weapon'))
        armor = equipment.get_armor(request.form.get('armor'))

        player_unit = Player(name=user_name, unit_class=unit_class, weapon=weapon, armor=armor)
        heroes['player'] = player_unit

        return redirect(url_for('Start.choose_enemy'))


@start_bp.route('/choose-enemy/', methods=['GET', 'POST'])
def choose_enemy():
    """Конфигурация сетапа врага"""

    if request.method == 'GET':
        result = {
            "header": 'Выбор героя для врага',
            "classes": unit_classes,
            "weapons": equipment.get_weapon_names(),
            "armors": equipment.get_armor_names()
        }

        return render_template('hero_choosing.html', result=result)

    if request.method == 'POST':
        user_name = request.form.get('name')
        unit_class = unit_classes[request.form.get('unit_class')]
        weapon = equipment.get_weapon(request.form.get('weapon'))
        armor = equipment.get_armor(request.form.get('armor'))

        enemy_unit = Enemy(name=user_name, unit_class=unit_class, weapon=weapon, armor=armor)
        heroes['enemy'] = enemy_unit

        return redirect(url_for('Fight.fight', _external=True))
