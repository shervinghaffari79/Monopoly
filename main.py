from tkinter import *
from PIL import Image, ImageTk
from Player import Player
from CreateProperty import Create


class Game:

  turn = "agent"

  def __init__(self, height, width):
    self.root = Tk()
    self.root['background'] = "pink"
    self.root.geometry("{}x{}".format(height, width))
    self.root.resizable(False, False)
    self.canvas = Canvas(self.root, width=660, height=660)
    self.start()

  def create_board(self):
    self.board = ImageTk.PhotoImage(Image.open('board.png').resize((660, 660)))
    self.logo = ImageTk.PhotoImage(Image.open('logo.png').resize((400, 152)))
    self.canvas.create_image(0, 0, image=self.board, anchor="nw")
    self.canvas.create_image(140, 300, image=self.logo, anchor="nw")
    self.canvas.grid(row=0, column=0)

  def player_turn(self):
    self.set_turn_lb()
    player.dice(Game.turn, agent)
    self.destroy_roll_button()
    Game.turn = "agent"

  def agent_turn(self):
    self.set_turn_lb()
    agent.dice(Game.turn, player)
    self.set_roll_button()
    Game.turn = "player"

  def start(self):
    self.create_board()
    self.init_dice()
    self.set_turn_lb()
    self.start_game()

  def start_game(self):
    self.start_game_button = Button(self.root,
                                    command=self.agent_turn,
                                    text="start",
                                    width=16,
                                    height=1,
                                    background="red",
                                    fg="white")
    self.start_game_button.place(x=260, y=200)

  def init_dice(self):
    self.dice_1 = ImageTk.PhotoImage(Image.open('6.png').resize((49, 49)))
    self.canvas.create_image(280, 120, image=self.dice_1, anchor="nw")

    self.dice_2 = ImageTk.PhotoImage(Image.open('6.png').resize((49, 49)))
    self.canvas.create_image(340, 120, image=self.dice_2, anchor="nw")

  def set_roll_button(self):
    self.set_turn_lb()
    self.roll = Button(self.root,
                       command=self.player_turn,
                       text="Roll Dice",
                       width=16,
                       height=1,
                       bg="red",
                       fg="white")
    self.roll.place(x=260, y=200)

  def destroy_roll_button(self):
    self.roll.destroy()
    self.end_turn_button = Button(self.root,
                                  command=self.agent_turn,
                                  text="End Turn",
                                  width=16,
                                  height=1,
                                  bg="red",
                                  fg="white")
    self.end_turn_button.place(x=260, y=200)

  def set_turn_lb(self):

    if Game.turn == "player":
      self.turn_lb = Label(self.root,
                           text="Player's turn",
                           foreground="black",
                           font="Arial",
                           bg="light blue",
                           width=14,
                           height=1).place(x=420, y=120)
    else:
      self.turn_lb = Label(self.root,
                           text="Agent's turn",
                           foreground="black",
                           font="Arial",
                           bg="light blue",
                           width=14,
                           height=1).place(x=420, y=120)


if __name__ == "__main__":

  game = Game(1100, 660)
  agent = Player(game.root, game.canvas, 750, 10, "hat.png")
  player = Player(game.root, game.canvas, 750, 350, "ship.png")
  agent.set_name("Agent")
  player.set_name("Player")
  cr = Create()
  game.root.mainloop()
