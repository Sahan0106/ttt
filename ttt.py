import turtle
tur = turtle.Turtle()
tur.color('red')
tur.speed(0)
tur.hideturtle()
tur.up()
def drawboard(game):
    for i in range(game.y-1):
        drawline([-game.size*game.x/2,game.size*game.y/2-(i+1)*game.size],[game.size*game.x/2,game.size*game.y/2-(i+1)*game.size])
    for i in range(game.x-1):
        drawline([game.size*game.x/2-(i+1)*game.size,-game.size*game.y/2],[game.size*game.x/2-(i+1)*game.size,game.size*game.y/2])
    
def drawline(a,b):
    tur.goto(a)
    tur.down()
    tur.goto(b)
    tur.up()
    
def drawshape(game,x,y):
    if game.turn=="o":
        tur.goto(-game.x*game.size/2-game.size/2+game.size*(y),game.y*game.size/2-game.size*0.9-game.size*(x-1))
        tur.down()
        tur.circle(game.size*0.4)
        tur.up()
    else:
        tur.goto(-game.x*game.size/2+game.size*0.1+game.size*(y-1),game.y*game.size/2-game.size*0.1-game.size*(x-1))
        tur.down()
        tur.goto(-game.x*game.size/2+game.size*0.9+game.size*(y-1),game.y*game.size/2-game.size*0.9-game.size*(x-1))
        tur.up()
        tur.goto(-game.x*game.size/2+game.size*0.1+game.size*(y-1),game.y*game.size/2-game.size*0.9-game.size*(x-1))
        tur.down()
        tur.goto(-game.x*game.size/2+game.size*0.9+game.size*(y-1),game.y*game.size/2-game.size*0.1-game.size*(x-1))
        tur.up()
//fuck you

class game():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 50
        self.board = [[0 for x in range(x)] for y in range(y)]
        self.player1="o"
        self.player2="x"
        self.turn="o"
        self.end=False
        self.winner=""
        drawboard(self)
 
def move(game,x,y):
    if game.board[x-1][y-1]==0:
        game.board[x-1][y-1]=game.turn    
        drawshape(game,x,y)
        if game.turn=="o":
            game.turn="x"
        else:
            game.turn="o"
        

game1 = game(3,3) 
while game1.end == False:
    i=input()
    x = int(i.split()[0])
    y = int(i.split()[1])
    move(game1,x,y)
    print(game1.board)

