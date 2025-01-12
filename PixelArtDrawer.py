import turtle as t
#Platformer Level
lev1 = [["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
      ["O", "O", "X", "X", "X", "X", "O", "O", "O", "O"],
      ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
      ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
      ["O", "X", "X", "O", "X", "X", "X", "O", "O", "O"],
      ["O", "O", "O", "O", "O", "O", "O", "O", "X", "X"],
      ["O", "O", "O", "O", "O", "O", "O", "O", "X", "X"],
      ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]]
#Mario
lev2 = [
   "WWWRRRRRRWWWW",
   "WWRRRRRRRRRRW",
   "WWTTTOOOKOWWW",
   "WTOTOOOOKOOOW",
   "WTOTTOOOOKOOG",
   "WTTOOOOOKKKKW",
   "WWWOOOOOOOOWW",
   "WWRRBRRBRWWWW",
   "WRRRBRRBRRRWW",
   "RRRRBBBBRRRRW",
   "OORBYBBYBROOW",
   "OOOBBBBBBOOOW",
   "OOBBBBBBBBOOW",
   "WWBBBWWBBBWWW",
   "WTTTWWWWTTTWW",
   "TTTTWWWWTTTTW",
]
tileSize = 50
class Tile():
   def __init__(self, x, y, color,size):
       self.x = x
       self.y = y
       self.color = color
       self.size = size
   def draw(self):
       tile = t.Turtle()
       tile.ht()
       tile.pu()
       tile.speed(0)
       tile.color(self.color)
       tile.goto(self.x, self.y)
       tile.begin_fill()
       for _ in range(4):
           tile.pd()
           tile.fd(self.size)
           tile.rt(90)
       tile.end_fill()
def drawLevel(l,xCor,y):
   for row in l:
       x = xCor
       for tile in row:
           if tile == "W" or tile == 1 :
               tile = Tile(x, y, "white", tileSize)
               tile.draw()
           elif tile == "R" or tile == 2 :
               tile = Tile(x, y, "red",  tileSize)
               tile.draw()
           elif tile == "T" or tile == 2 :
               tile = Tile(x, y, "brown", tileSize)
               tile.draw()
           elif tile == "O" or tile == 2 :
               tile = Tile(x, y, "orange", tileSize)
               tile.draw()
           elif tile == "K" or tile == 2 :
               tile = Tile(x, y, "black", tileSize)
               tile.draw()
           elif tile == "y" or tile == 2 :
               tile = Tile(x, y, "yellow", tileSize)
               tile.draw()
           elif tile == "B" or tile == 2 :
               tile = Tile(x, y, "blue", tileSize)
               tile.draw()
           x+=tileSize
       y-=tileSize
#Setting up the Screen & Drawing the Level
sc = t.Screen()
sc.bgcolor("black")
def setup(lev, mode):
   if mode == 1:
       t.tracer(0, 0)
       sc.setup(width=(len(lev[0])*tileSize ), height=(len(lev)*tileSize))
       sc._root.resizable(False, False)
       drawLevel(lev, -(len(lev[0])*tileSize)/2, (len(lev)*tileSize)/2)
       t.tracer(1)
   elif mode == 2:
       sc.setup(width=(len(lev[0])*tileSize ), height=(len(lev)*tileSize))
       sc._root.resizable(False, False)
       drawLevel(lev, -(len(lev[0])*tileSize)/2, (len(lev)*tileSize)/2)
setup(lev2, 2)
sc.mainloop()
