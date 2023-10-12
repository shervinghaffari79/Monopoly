from tkinter import *
from PIL import Image ,ImageTk

class Property :

    def __init__(self,name,price,rent,x,y,image,type):
        self.name = name
        self.HouseNo = 0
        self.rent = rent
        self.price = price
        self.owner = None
        self.can_buy = True
        self.x = x
        self.y = y
        self.image = image
        self.type = type


    def display(self):

        self.set_main_root()

        self.set_image()

        self.set_over_layer("pink")

        self.set_button()

        self.root2.mainloop()

    def set_main_root(self):
        self.root2 = Toplevel()
        self.root2.geometry("600x450")
        self.root2.title("Property")
        self.root2.resizable(False, False)

    def set_over_layer(self,background):
        canvas = Canvas(self.root2, width=600, height=450)
        canvas.create_image(300, 20, image=self.card, anchor="nw")
        canvas.create_image(45, 50, image=self.offer, anchor="nw")

        canvas.grid(row=0, column=0)
        canvas.configure(background=background)

    def set_image(self):
        self.offer = ImageTk.PhotoImage(Image.open('offer.png').resize((234, 343)))
        self.card = ImageTk.PhotoImage(Image.open(self.image).resize((250, 350)))

    def set_button(self):

        Button(self.root2, text="Pass", command=self.Pass, width=13, height=1, bg="orange", fg="white").place(x=310,
                                                                                                              y=380)
        if self.get_type() == "house":
            if self.get_Owner() != None:
                self.sell_button = Button(self.root2, text="Sell", command=self.sell_property, width=32, height=1,
                                          bg="orange", fg="white").place(x=310, y=415)

            self.purchase = Button(self.root2, text="Purchase", command=self.purchase_handler, width=13, height=1, bg="orange",
                          fg="white")
            self.purchase.place(x=440, y=380)

    def get_type(self):
        return self.type

    def purchase_handler(self):

        self.purchase.destroy()

        if not self.owner :
            self.Mo = Button(self.root2, text="Mortgage", command=self.Mortgage, width=13, height=1, bg="orange",fg="white")
            self.Mo.place(x=440, y=380)

        elif(self.HouseNo != 4):

            self.house = Button(self.root2, text="House", command=" ", width=13, height=1, bg="orange",
                                fg="white")
            self.house.place(x=440, y=380)
        else:
            self.hotel = Button(self.root2, text="Hotel", command=" ", width=13, height=1, bg="orange",
                                fg="white")
            self.hotel.place(x=440, y=380)

    def Buy_House(self):
        pass


    def Buy_Hotel(self):
        pass

    def set_layer(self,root):
        self.layer = root

    def sell_offer(self):
        self.set_Owner(None)
        self.active_player.get_sell_prop_money(self.get_price(), self.get_name())
        if self.active_player.property.get_type() == "tax":
            self.active_player.pay_tax(self.active_player.property.get_tax())
        elif self.active_player.property.get_type() == "house":
            self.active_player.pay_rent(self.active_player.property.get_rent())
        self.layer.destroy()

    def sell_property(self):
        self.set_Owner(None)
        self.active_player.get_sell_prop_money(self.get_price(),self.get_name())
        if self.active_player.get_name() == "Player":
            self.root2.destroy()

    def Mortgage(self):
        self.active_player.Mortgage(self.price)
        self.set_Owner(self.active_player.get_name())
        self.root2.destroy()

    def Pass(self):

        if self.root2:
            self.root2.destroy()

    def set_roll(self):
        self.root2.destroy()

    def destroy_roll(self):
        self.roll.destroy()

    def is_available(self):
        if self.get_Owner():
            return False
        else:
            return True

    def get_Owner(self):
        return self.owner

    def set_Owner(self,name):
        self.owner = name

    def get_name(self):
        return self.name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_rent(self,rent):
        self.rent = rent

    def get_rent(self):
        return self.rent

    def get_price(self):
        return self.price

    def set_active_player(self,player):
        self.active_player = player
