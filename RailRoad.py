from Property import Property
from tkinter import *

class RailRoad(Property):

    color = "light green"

    def __init__(self,x,y,price,rent,name,image,type):

        super().__init__(name,price,rent,x,y,image,type)


    def display(self):

        self.set_main_root()
        self.set_image()
        self.set_over_layer(RailRoad.color)
        self.set_button()
        self.root2.mainloop()

    def set_button(self):

        Button(self.root2, text="Pass", command=self.Pass, width=13, height=1, bg="red",fg="white").place(x=310,y=380)
        if self.get_Owner() != None:
            self.sell_button = Button(self.root2, text="Sell", command=self.sell_property, width=13, height=1,
                                      bg="orange", fg="white").place(x=440, y=380)
        else:
            self.purchase = Button(self.root2,text="Buy",command=self.Mortgage,width=13,height=1,bg="red",fg="white")
            self.purchase.place(x=440,y=380)