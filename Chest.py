import random


class chest:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.set_prize()

    def set_prize(self):
        self.prizes = [5,20,0,40,15,10,25,30,35,45]
        random.shuffle(self.prizes)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_type(self):
        return "chest"

    def get_prize(self,player):
        prize = self.prizes[random.randint(0,5)]
        player.get_chance_money(prize)
        player.log_lb(f"{player.get_name()} you found {prize}$ in chest")
