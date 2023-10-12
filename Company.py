from RailRoad import RailRoad

class Company(RailRoad):

    def __init__(self,name,price,x,y,rent,image,type):
        super().__init__(name,price,rent,x,y,image,type)


