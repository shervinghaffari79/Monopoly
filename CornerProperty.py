
class Corner:

    def __init__(self,x,y,name,type):
        self.x = x
        self.y = y
        self.name = name
        self.type=type

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type