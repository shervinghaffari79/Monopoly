import random
from tkinter import *
from CreateProperty import Create
from PIL import Image, ImageTk

class Player :

    number = 0

    def __init__(self,root,canvas,LX,LY,img):
        Player.number+=1
        self.counter = 0
        self.x ,self.y = -10 , 10
        self.LX ,self.LY ,self.LX_temp,self.LY_temp = LX,LY,LX,LY
        self.num  = 0
        self.root = root
        self.canvas = canvas
        self.img = Image.open(img)
        self.set_Piece()
        self.cash = 100
        self.worth = self.cash
        self.in_jail = False
        self.chance = False
        self.reverse = False



    def set_Lable(self):
        self.title = Label(self.root, text=self.get_name(), font="Arial", foreground="black",
                              bg="light blue", borderwidth=5
                              , width=12, height=1).place(x=self.LX, y=self.LY)
        self.set_Piece()
        self.set_cash_lb()

    def set_cash_lb(self):

        self.lable = Label(self.root, text=f"Cash : {self.get_cash()}$", font="Arial", foreground="black",
                           bg="light blue", borderwidth=5
                           , width=15, height=1).place(x=self.LX+140, y=self.LY)

    def update_cash(self):
        self.update = Label(self.root, text=f"Cash : {self.get_cash()}$", font="Arial", foreground="black",
                           bg="light blue", borderwidth=5
                           , width=15, height=1).place(x=self.LX+140, y=self.LY)

    def set_name(self,name):
        self.name = name
        self.set_Lable()

    def get_name(self):
        return self.name

    def get_cash(self):
        return self.cash

    def add_cash(self):
        self.cash+=200
        self.update_cash()

    def sell_offer(self):
        self.layer = Toplevel()
        self.layer['background'] = "light blue"
        x = 10
        y = 10
        self.layer.geometry("600x300")
        self.layer.title("Sell offer")
        for property in Create.PropertyList:
            if (property.get_type()=="house" or property.get_type()=="Company" or property.get_type()=="railroad") and property.get_Owner() == self.get_name():
                property.set_layer(self.layer)
                Button(self.layer,text=property.get_name(),command=property.sell_offer,width=13,height=1,bg="orange",fg="white").place(x=x,y=y)
                x+=120
                if x>500:
                    x=10
                    y+=80
        self.layer.mainloop()

    def Mortgage(self,price):
        if self.property.get_type() == "railroad":
            self.property.set_rent(Create.get_rail_road_rent(Create, self.get_name()))

        if self.get_cash()>=price:
            self.cash-=price
            self.update_cash()
            self.add_house_tag()
            self.log_lb(f"{self.get_name()} has bought {self.property.get_name()}")
        else:
            self.property.root2.destroy()
            self.log_lb(f"{self.get_name()} has no sufficient credit")
            self.sell_offer()


    def add_house_tag(self):
        if self.LY_temp <self.LY+250 :
            self.LY_temp+=50
        else:
            self.LY_temp=self.LY+50
            self.LX_temp+=100

        self.tag = Label(self.root, text=self.property.get_name(), background="pink", fg="black", width=16,
                         height=1).place(x=self.LX_temp, y=self.LY_temp)


    def pay_rent(self,rent):
        if self.property.get_type() == "Company":
            self.property.set_rent(Create.get_company_rent(Create, self.temp.get_name(),self.total))

        self.log_lb(f"{self.get_name()}, you have pay {self.property.get_rent()} for rent")
        if self.cash < rent:
            self.sell_offer()
        else:
            self.cash-=rent
            self.update_cash()

    def get_rent(self,rent):
        self.cash+=rent
        self.update_cash()

    def get_chance_money(self,money):
        self.cash+=money
        self.update_cash()

    def get_sell_prop_money(self,money,prop):
        self.cash += money
        self.update_cash()
        self.log_lb(f"{self.get_name()} has sold {prop}!")

    def set_Piece(self):

        self.piece = ImageTk.PhotoImage(self.img.resize((40,40)))

        self.player = self.canvas.create_image(40,40,image = self.piece,anchor = "nw")



    def dice(self,turn,temp):

        self.temp = temp

        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        self.set_dice_lb(dice1,dice2)

        self.turn = turn

        self.total = dice1+dice2

        if self.is_in_jail() :
            if dice1 == dice2:
                self.log_lb(f"{self.get_name()}, you rolled double thus you're free to go")
                self.set_out_jail()
                self.movement()
        else:
            self.movement()


    def pay_tax(self,tax):
        if self.cash>=tax:
            self.cash-=tax
            self.log_lb(f"{self.get_name()} paid {tax} $ for tax")
            self.update_cash()
        else:
            self.sell_offer()


    def set_dice_lb(self,dice1,dice2):

        self.dice1_lb = Label(self.root, text="Dice1 : {}".format(dice1), font="Arial",foreground="black", bg="light blue",borderwidth=5
            ,width=12, height=1).place(x=110, y=120)

        self.dice1_lb = Label(self.root, text="Dice2 : {}".format(dice2),font="Arial" ,foreground="black", bg="light blue",borderwidth=5
            ,width=12, height=1).place(x=110, y=160)

        self.dice_1 = ImageTk.PhotoImage(Image.open('{}.png'.format(dice1)).resize((48, 48)))
        self.canvas.create_image(280, 120, image=self.dice_1, anchor="nw")

        self.dice_2 = ImageTk.PhotoImage(Image.open('{}.png'.format(dice2)).resize((48, 48)))
        self.canvas.create_image(340, 120, image=self.dice_2, anchor="nw")

    def set_current(self,player):
      self.current = player

    def get_current(self):
      return self.current

    def evaluation(self,board):
        curr_player = self.get_current()
        score = 0

        score += curr_player.get_cash()

        for property in board :
          
          if property.get_type() == "house" and property.get_Owner() == curr_player.get_name():
            score += 2*property.get_price()
            
          elif property.get_type() == "railroad" and property.get_Owner() == curr_player.get_name():
            score+= 3*property.get_price()

          elif property.get_type() == "Company" and property.get_Owner() == curr_player.get_name():
            score += 4*property.get_price()
            
          elif self.is_in_jail():
            score -= 30
            
        return score
            

    def Expectimax(self,depth,board,is_maximizing):

        if depth == 0 :
            return self.evaluation(board)

        if is_maximizing:
            best_score = -float('inf')
            best_action = None
            self.set_current(self)
            for action in ['buy','pass','sell']:
              
              new_board = self.apply_action(action,self,board)
              score = self.Expectimax(depth-1,new_board,False)
              if score > best_score:
                score = best_score
                best_action = action
                
            return best_action
              

        else:
            total_score = 0
            num_actions = 0
            self.set_current(self.temp)
            for action in ['buy','pass','sell']:
              
              new_board = self.apply_action(action,self.temp,board)

              total_score+= self.Expectimax(depth-1,new_board,True)

              num_actions+=1

            return total_score/num_actions

    def apply_action(self,action,board,maximizing):
      # if cuurent player is minimizer roll the dice and make action
      if action == "buy":
        pass
      elif action == "pass":
        pass
      else:
        pass


    def go_to_jail(self):
        self.piece = None
        self.piece = ImageTk.PhotoImage(self.img.resize((40, 40)))
        self.player = self.canvas.create_image(600, 40, image=self.piece, anchor="nw")
        self.x , self.y = 0,10
        self.log_lb(f"{self.get_name()}, you have to go to the jail")
        self.in_jail = True


    def log_lb(self,text):
        self.log_lable = Label(self.root, text=text,font = "Arial",background="light blue",fg="black",width=50,height=1)
        self.log_lable.place(x=100, y=500)

    def set_in_jail(self):
        self.in_jail = True

    def set_out_jail(self):
        self.in_jail = False

    def is_in_jail(self):
        if self.in_jail :
            return True
        else:
            return False

    def start(self):
        self.add_cash()

    def set_chance_x_y(self,x,y):
        self.chance_x = x
        self.chance_y = y

    def chance_movement(self):

        if self.x == self.chance_x and self.y == self.chance_y:
                self.chance = False
                self.reverse = False
                self.property_handler(Create.find_property(Create, self.x, self.y))
                return
        self.move()


    def movement(self):

        if self.counter == self.total:
            self.counter=0
            self.reverse=False
            self.property_handler(Create.find_property(Create, self.x, self.y))
            return

        self.move()


    def move(self):

        if self.y < 10 and self.x == -10:

            if self.reverse:
                self.move_down()
            else:
                self.move_up()

        elif self.y == 10 and self.x < 0:

            if self.reverse:
                self.move_left()
            else:
                self.move_right()

        elif self.y > 0 and self.x == 0:

            if self.reverse:
                self.move_up()
            else:
                self.move_down()

        elif self.y == 0 and self.x > -10:

            if self.reverse:
                self.move_right()
            else:
                self.move_left()

        if self.x == -10 and self.y == 10:
            self.start()

        if self.chance:
            self.canvas.after(300, self.chance_movement)
        else:
            self.canvas.after(300, self.movement)

    def property_handler(self,property):

        self.property = property

        if self.property.get_type() == "corner":

            if self.property.get_name() == "jail":
                self.go_to_jail()


        elif self.property.get_type() == "tax":
                self.pay_tax(self.property.get_tax())

        elif self.property.get_type() == "chance":

            self.property.set_chance_button(self)

        elif self.property.get_type() == "chest":
            self.property.get_prize(self)

        else:

            if self.property.get_Owner() == None:
                self.property.set_active_player(self)

                # player decides to buy or pass the property
                if self.get_name() == "Player":
                    self.property.display()

                # agent decides to buy or pass the property
                else:
                    self.new_board = Create.PropertyList.copy()
                    self.max_x = self.x
                    self.max_y = self.y
                    self.min_x = self.temp.x
                    self.min_y = self.temp.y
                    # self.Expectimax(2,self.new_board,True)

            elif self.get_name() == self.property.get_Owner():

                self.property.set_active_player(self)

                # player decides to keep or sell its property
                if self.get_name() == "Player":
                    self.property.display()

                # agent decides to keep or sell its property
                else:
                    pass
            # agent or player has to pay rent
            else:
                self.property.set_active_player(self)
                self.pay_rent(self.property.get_rent())
                self.temp.get_rent(self.property.get_rent())
                self.temp.update_cash()



    def move_left(self):

        if self.x == 0 or self.x==-9:

            self.canvas.move(self.player,-68,0)

        else:

            self.canvas.move(self.player, -51, 0)

        self.x-=1
        if not self.chance:
            self.counter+=1


    def move_right(self):
        if self.x == -10 or self.x == -1:

            self.canvas.move(self.player, 68, 0)
        else:

            self.canvas.move(self.player, 51, 0)

        self.x+=1
        if not self.chance:
            self.counter += 1


    def move_up(self):

        if self.y == 0 or self.y == 9:

            self.canvas.move(self.player, 0, -68)
        else:

            self.canvas.move(self.player, 0, -51)

        self.y += 1
        if not self.chance:
            self.counter += 1

    def move_down(self):
        if self.y == 1 or self.y == 10:

            self.canvas.move(self.player, 0, 68)
        else:

            self.canvas.move(self.player, 0, 51)
        self.y -= 1
        if not self.chance:
            self.counter += 1
