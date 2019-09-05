from django.db import models


# Create your models here.


class Castle(models.Model):
    castle_name = models.CharField(max_length=40)
    hero_attack_bonus = models.IntegerField()
    hero_defence_bonus = models.IntegerField()

    def __str__(self):
        return self.castle_name

    @property
    def small_castle_picture_path(self):
        return "small_images/Town_portrait_{name}_small.gif".format(name=self.castle_name)
        # <img src="{% static castle.small_castle_picture_path %}">


class Creature(models.Model):
    name = models.CharField(max_length=64)
    castle_name = models.ForeignKey(Castle, on_delete=models.CASCADE)
    lvl = models.CharField(max_length=8)
    attack = models.IntegerField()
    defence = models.IntegerField()
    min_dmg = models.IntegerField()
    max_dmg = models.IntegerField()
    health = models.IntegerField()
    speed = models.IntegerField()
    growth = models.IntegerField()
    fight_value = models.IntegerField()
    AI_value = models.IntegerField()
    special_abilities = models.CharField(max_length=512)

    @property
    def small_creature_picture_path(self):
        return "small_images/Creature_portrait_{name}_small.gif".format(name=self.name.replace(' ', '_'))
        # <img src="{% static creature.small_picture_path %}">
