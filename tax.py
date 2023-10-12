
class tax:
    def __init__(self,x,y,tax,type):
        self.x = x
        self.y = y
        self.tax = tax
        self.type = type

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_type(self):
        return self.type

    def get_tax(self):
        return self.tax

    def tax_type(self):
        return self.type
