from tkinter import PhotoImage
class Cards:

    def __init__(self,photo,command,data):
        self.photo = PhotoImage(file = photo)
        self.command = command
        self.data = data

    def get_photo(self):
        return self.photo

    def get_command(self):
        return self.command

    def get_data(self):
        return self.data

    def get_x(self):
        return self.data.get("x")

    def get_y(self):
        return self.data.get("y")