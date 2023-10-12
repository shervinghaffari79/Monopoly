from Property import Property
from PIL import Image ,ImageTk
from CornerProperty import Corner
from RailRoad import RailRoad
from Company import Company
from tax import tax
from Chance import Chance
from  Chest import chest
class Create :

    PropertyList = []
    Image.open("Baltic.png")
    def __init__(self):
        self.Atlantic = Property("Atlantic",130,180,-6,0,"Atlantic.png","house")
        self.NewYork = Property("NewYork",100,16,0,1,"NewYork.png","house")
        self.Baltic = Property("Baltic",30,4,-7,10,"Baltic.png","house")
        self.Boardwalk = Property("Boardwalk",200,50,-10,9,"Boardwalk.png","house")
        self.Conn = Property("Connecticut",60,8,-1,10,"Conn.png","house")
        self.ILLI = Property("Iliinois",120,20,-4,0,"ILIINOIS.png","house")
        self.Indiana = Property("Indiana",110,18,-3,0,"Indiana.png","house")
        self.Kentacky = Property("Kentacky",110,18,-1,0,"Kentacky.png","house")
        self.Marvin = Property("Marvin",140,24,-9,0,"Marvin.png","house")
        self.Medi = Property("Mediterranean",30,2,-9,10,"Medi.png","house")
        self.North = Property("North Carolina",150,26,-10,2,"North.png","house")
        self.Oriental = Property("Oriental",50,6,-4,10,"Oriental.png","house")
        self.Pacific = Property("Pacific", 150, 26, -10, 1, "Pacific.png","house")
        self.Park = Property("Park", 175, 35, -10, 7, "Park.png","house")
        self.Pennsylvania = Property("Pennsylvania", 160, 28, -10, 4, "Pennsylvania.png","house")
        self.States = Property("States", 70, 10, 0, 7, "States.png","house")
        self.StCharles = Property("StCharles", 70, 10, 0, 9, "StCharles.png","house")
        self.StJames = Property("StJames", 90, 14, 0, 4, "StJames.png","house")
        self.Tenn = Property("Tennessee", 90, 14, 0, 2, "Tenn.png","house")
        self.Ventnor = Property("Ventnor", 130, 29, -7, 0, "Ventnor.png","house")
        self.Vermont = Property("Vermont", 50, 6, -2, 10, "Vermont.png","house")
        self.Virginia = Property("Virginia", 80, 12, 0, 6, "Virginia.png","house")
        self.jail = Corner(-10,0,"jail","corner")
        self.start = Corner(-10, 10, "start","corner")
        self.parking = Corner(0,0,"parking","corner")
        self.visit = Corner(0,10,"visit","corner")
        self.reading_railroad = RailRoad(-5,10,200,25,"Reading railroad","reading-railroad.jpg","railroad")
        self.pennsylvania_railroad = RailRoad(0,5,200,25,"Pennsylvania railroad","pennsylvania-railroad.jpg","railroad")
        self.b_and_o_railroad = RailRoad(-5,0,200,25,"B &  O railroad","b-and-o-railroad.jpg","railroad")
        self.short_line = RailRoad(-10, 5, 200, 25, "Short Line", "short-line-railroad.jpg","railroad")
        self.tax = tax(-6, 10, 200, "tax")
        self.luxury_tax = tax(-10, 8, 100, "tax")
        self.electric = RailRoad(0, 8, 150, 25, "Electric Company", "electric-company.jpg", "Company")
        self.water_works = RailRoad(-8, 0, 150, 25, "Water Works", "water-works.jpg", "Company")
        self.chance1 = Chance(-3, 10)
        self.chance2 = Chance(-2, 0)
        self.chance3 = Chance(-10, 6)
        self.chest1 = chest(-8,10)
        self.chest2 = chest(0, 3)
        self.chest3 = chest(-10, 3)
        self.add_to_list()

    def add_to_list(self):
        Create.PropertyList.append(self.Medi)
        Create.PropertyList.append(self.chest1)
        Create.PropertyList.append(self.Baltic)
        Create.PropertyList.append(self.tax)
        Create.PropertyList.append(self.reading_railroad)
        Create.PropertyList.append(self.Oriental)
        Create.PropertyList.append(self.Vermont)
        Create.PropertyList.append(self.chance1)
        Create.PropertyList.append(self.Conn)
        Create.PropertyList.append(self.visit)
        Create.PropertyList.append(self.StCharles)
        Create.PropertyList.append(self.electric)
        Create.PropertyList.append(self.States)
        Create.PropertyList.append(self.Virginia)
        Create.PropertyList.append(self.pennsylvania_railroad)
        Create.PropertyList.append(self.StJames)
        Create.PropertyList.append(self.chest2)
        Create.PropertyList.append(self.Tenn)
        Create.PropertyList.append(self.NewYork)
        Create.PropertyList.append(self.parking)
        Create.PropertyList.append(self.Kentacky)
        Create.PropertyList.append(self.chance2)
        Create.PropertyList.append(self.Indiana)
        Create.PropertyList.append(self.ILLI)
        Create.PropertyList.append(self.b_and_o_railroad)
        Create.PropertyList.append(self.Atlantic)
        Create.PropertyList.append(self.Ventnor)
        Create.PropertyList.append(self.water_works)
        Create.PropertyList.append(self.Marvin)
        Create.PropertyList.append(self.jail)
        Create.PropertyList.append(self.Pacific)
        Create.PropertyList.append(self.North)
        Create.PropertyList.append(self.chest3)
        Create.PropertyList.append(self.Pennsylvania)
        Create.PropertyList.append(self.short_line)
        Create.PropertyList.append(self.chance3)
        Create.PropertyList.append(self.Park)
        Create.PropertyList.append(self.luxury_tax)
        Create.PropertyList.append(self.Boardwalk)
        Create.PropertyList.append(self.start)

    def find_property(self,x,y):

        for property in Create.PropertyList:
            if x == property.get_x() and y == property.get_y():
                return property

    def get_rail_road_rent(self,name):
        number = 1
        for railroad in Create.PropertyList:
            if railroad.get_type()=="railroad" and railroad.get_Owner() == name:
                number+=1

        return 25*number

    def get_company_rent(self,name,total_dice):
        number = 0
        for company in Create.PropertyList:
            if company.get_type() == "Company" and company.get_Owner() == name:
                number +=1

        return total_dice * 4 if number==1 else total_dice*10



