import json
import requests
from bs4 import BeautifulSoup

page_with_stats = requests.get('http://heroes.thelazy.net/wiki/List_of_creatures')
soup_creatures_stats = BeautifulSoup(page_with_stats.content, 'html.parser')
creatures_stats = soup_creatures_stats.select("body table tr")

page_with_fight_value = requests.get('http://heroes.thelazy.net/wiki/AI_value')
soup_fight_value = BeautifulSoup(page_with_fight_value.content, 'html.parser')
creatures_fight_value = soup_fight_value.select("body table tr")

fight_value_dict = {}
for i in range(2, 148):
    creature_name = creatures_fight_value[i].find_all('td')[1].find_all('a')[1].get_text()
    creature_fight_value = creatures_fight_value[i].find_all('td')[3].get_text().strip()
    fight_value_dict.update({f'{creature_name}': creature_fight_value})


class Creature:
    def __init__(self, creature_statistics):
        self.name = creature_statistics.find_all('td')[0].find_all('a')[1].get_text().strip()
        self.castle = creature_statistics.find('span').attrs['title']
        self.lvl = creature_statistics.find_all('td')[2].get_text().strip()[0:2]
        self.attack = int(creature_statistics.find_all('td')[3].find('span').get_text().strip())
        self.defence = int(creature_statistics.find_all('td')[4].find('span').get_text().strip())
        self.min_dmg = int(creature_statistics.find_all('td')[5].find('span').get_text().strip())
        self.max_dmg = int(creature_statistics.find_all('td')[6].find('span').get_text().strip())
        self.health = int(creature_statistics.find_all('td')[7].find('span').get_text().strip())
        self.speed = int(creature_statistics.find_all('td')[8].find('span').get_text().strip())
        self.growth = int(creature_statistics.find_all('td')[9].find('span').get_text().strip())
        self.fight_value = int(fight_value_dict[f'{self.name}'])
        self.AI_value = int(creature_statistics.find_all('td')[10].find('span').get_text().strip())
        self.special_abilities = creature_statistics.find_all('td')[13].get_text().strip()


creature_list = []
for i in range(1, len(creatures_stats)):
    unit = Creature(creatures_stats[i])
    creature_list.append({
        'Creature': unit.name,
        'Castle': unit.castle,
        'Level': unit.lvl,
        'Attack': unit.attack,
        'Defence': unit.defence,
        'Min dmg': unit.min_dmg,
        'Max dmg': unit.max_dmg,
        'Health': unit.health,
        'Speed': unit.speed,
        'Growth': unit.growth,
        'Fight_value': unit.fight_value,
        'AI_value': unit.AI_value,
        'Special abilities': unit.special_abilities
    })

with open('creatures.json', 'w') as f:
    f.write(json.dumps(creature_list))
