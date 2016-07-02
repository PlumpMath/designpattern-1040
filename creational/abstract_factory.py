

class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        msg = "{} the Frog encounters {} and {}.".format(self, obstacle, obstacle.action())
        print(msg)


class Bug:
    def __str__(self):
        return "a bug"

    def action(self):
        return "eats it"


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n\n\t----- Frog World -----"

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


