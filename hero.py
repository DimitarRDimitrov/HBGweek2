from entity import Entity


class Hero(Entity):

    def __init__(self, name, health, nickname):
        self.name = name
        self.health = health
        self.nickname = nickname
        self._MAX_HEALTH = health

    def known_as(self):
        return "{} the {}".format(self.name, self.nickname)
        # return self.name + " the " + self.nickname

