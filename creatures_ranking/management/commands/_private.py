from creatures_ranking.models import Castle, Creature
import json


def create_castles():
    Castle.objects.create(castle_name='Castle', hero_attack_bonus=2, hero_defence_bonus=2)
    Castle.objects.create(castle_name='Rampart', hero_attack_bonus=1, hero_defence_bonus=3)
    Castle.objects.create(castle_name='Tower', hero_attack_bonus=1, hero_defence_bonus=1)
    Castle.objects.create(castle_name='Inferno', hero_attack_bonus=2, hero_defence_bonus=2)
    Castle.objects.create(castle_name='Necropolis', hero_attack_bonus=1, hero_defence_bonus=2)
    Castle.objects.create(castle_name='Dungeon', hero_attack_bonus=2, hero_defence_bonus=2)
    Castle.objects.create(castle_name='Stronghold', hero_attack_bonus=4, hero_defence_bonus=0)
    Castle.objects.create(castle_name='Fortress', hero_attack_bonus=0, hero_defence_bonus=4)
    Castle.objects.create(castle_name='Conflux', hero_attack_bonus=3, hero_defence_bonus=1)
    Castle.objects.create(castle_name='Neutral', hero_attack_bonus=0, hero_defence_bonus=0)


def creatures():
    with open('creatures.json', 'r') as f:
        return json.loads(f.read())


def create_creatures():
    creatures_list = creatures()
    for monster in creatures_list:
        Creature.objects.create(name=monster['Creature'],
                                castle_name=Castle.objects.get(castle_name=monster['Castle']),
                                lvl=monster['Level'],
                                attack=monster['Attack'],
                                defence=monster['Defence'],
                                min_dmg=monster['Min dmg'],
                                max_dmg=monster['Max dmg'],
                                health=monster['Health'],
                                speed=monster['Speed'],
                                growth=monster['Growth'],
                                fight_value=monster['Fight_value'],
                                AI_value=monster['AI_value'],
                                special_abilities=monster['Special abilities'])
