import random
from tkinter import *
from Chance_Cards import Cards

class Chance:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.set_cards()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_chance_button(self,player):
        self.player = player

        if player.get_name() == "Player":
            self.chance_button = Button(player.root, text="Chance", command=self.display,width=19,height=1
                                    ,bg="red",foreground="white",borderwidth=1)
            self.chance_button.place(x=260, y=260)
        else:
            self.randomChoice = random.randint(0,7)
            print(self.randomChoice)
            self.cards[self.randomChoice].get_command()()

    def display(self):

        self.root = Toplevel()
        self.root.resizable(False,False)
        self.root.geometry("350x205")
        self.randomChoice = random.randint(0,7)
        self.button = Button(self.root,command=self.cards[self.randomChoice].get_command(),image = self.cards[self.randomChoice].get_photo(),width=344,height=200)\
            .grid(row=0,column=0)
        self.root.mainloop()

    def get_type(self):

        return "chance"

    def set_cards(self):

       self.cards = [Cards("advance_to_go.png",self.go_to,{"x":-10,"y":10,"name":"start"}),
                     Cards("go_to_broadwalk.png",self.go_to,{"x":-10,"y":9,"name":"Broadwalk"}),
                     Cards("go_to_reading.png",self.go_to,{"x":-5,"y":10,"name":"Reading"}),
                     Cards("st.charles.png",self.go_to,{"x":0,"y":9,"name":"St.Charles"}),
                    Cards("bank_pay_50.png", self.get_money, {"money": 50}),
                    Cards("collect150.png", self.get_money, {"money": 150}),
                    Cards("pay_tax.png", self.pay_money, {"tax": 15}),
                    Cards("go_back.png", self.go_reverse, {"spaces": 3})
                     ]

    def go_to(self):
        if self.player.get_name() == "Player":
            self.root.destroy()
            self.chance_button.destroy()
        self.player.chance = True
        self.player.log_lb(f"{self.player.get_name()} you have to go {self.cards[self.randomChoice].get_data().get('name')}")
        self.player.set_chance_x_y(self.cards[self.randomChoice].get_x(),self.cards[self.randomChoice].get_y())
        self.player.chance_movement()

    def go_reverse(self):
        self.player.reverse = True
        self.player.log_lb(f"{self.player.get_name()} you have to go 3 spaces back")
        self.player.total = self.cards[self.randomChoice].get_data().get("spaces")
        self.player.movement()

        if self.player.get_name() == "Player":
            self.root.destroy()
            self.chance_button.destroy()


    def get_money(self):
        if self.player.get_name() == "Player":
            self.root.destroy()
            self.chance_button.destroy()
        money = self.cards[self.randomChoice].get_data().get("money")
        self.player.log_lb(f"{self.player.get_name()} you got {money}$")
        self.player.get_chance_money(money)

    def pay_money(self):
        if self.player.get_name() == "Player":
            self.root.destroy()
            self.chance_button.destroy()
        self.player.pay_tax(self.cards[self.randomChoice].get_data().get("tax"))