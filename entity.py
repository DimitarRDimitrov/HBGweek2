from weapon import Weapon


class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = health
        self.weapon = "default"

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def take_damage(self, damage):
        if self.health < damage:
            self.health = 0
        else:
            self.health -= damage

    def take_healing(self, healing_points):
        if self.health == 0:
            return False
        elif self.health + healing_points > self._MAX_HEALTH:
            self.health = self._MAX_HEALTH
            return True
        else:
            self.health += healing_points
            return True

    def has_weapon(self):
        if self.weapon != "default":
            return True
        else:
            return False

    def equip_weapon(self, wep_name):
        self.weapon = wep_name

    def attack(self):
        if self.weapon == "default":
            return 0
        elif self.weapon.critical_hit():
            return self.weapon.damage*2
        else:
            return self.weapon.damage


