#This is the full annotated code for adventureCirle

#These import function call Tkinter, Python's standard GUI
#and random, to generate random numbers
from tkinter import * 
from random import *

#The game is held under one class
class adventureCircle:

#The subroutine that creates the interface and places the widgets
    def __init__(self):
        self.root=Tk()
        self.RUN=False
        
        self.frame=Frame(bg="black")
        self.frame.pack()
        
        self.Canvas=Canvas(self.frame, bg="black",width=300,height=300)
        self.Canvas.pack()

        self.root.resizable(0, 0)
        
        self.TimerText=Label(self.frame, bg="black", fg="white")
        self.TimerText.pack()
        self.PointsText=Label(self.frame, bg="black", fg="white")
        self.PointsText.pack()
        self.Title=Label(self.frame, bg="black", fg="white", text="Welcome to adventureCircle!")
        self.Title.pack()
        self.Instructions=Label(self.frame, bg="black", fg="white", text="Click on the screen to move the circle.")
        self.Instructions.pack()
        self.Instructions=Label(self.frame, bg="black", fg="white", text="Consume the green items and avoid the red ones.")
        self.Instructions.pack()
        self.Instructions=Label(self.frame, bg="black", fg="white", text="Look out for yellow power-ups!")
        self.Instructions.pack()
        self.PlayButton=Button(self.frame, bg="black", fg="white", text="Play" ,command=self.start)
        self.PlayButton.pack()
        
        self.root.mainloop()

#The subroutine that initialises all components when the play button is pressed
    def start(self):
        self.Timer=0
        self.RUN=True
        
        self.GoodItemX=[]
        self.GoodItemY=[]

        self.BadItemX=[]
        self.BadItemY=[]

        self.PowerUpItemX=[[],[]]
        self.PowerUpItemY=[[],[]]

        self.Points=0
        
        self.x=100
        self.y=100
        self.tempx=100
        self.tempy=100
        self.UP=False
        self.DOWN=False
        self.LEFT=False
        self.RIGHT=False

        self.Size=3
        self.Canvas.bind("<ButtonPress-1>", self.MouseClicks)
        self.run()

    def run(self):
        if self.RUN is True:
            self.Timer+=1
            self.TimerText['text']="Time: " + str(self.Timer//100)
            self.PointsText['text']="Points: " + str(self.Points)
            self.MoveCircleSprite(10*self.Size,2)
            self.paint()
            self.root.after(10, self.run)

#Subroutine that ends the game once it is game over
    def end(self):
        self.RUN=False
        self.Canvas.unbind("<ButtonPress-1>")

#Subroutine for the good item 
    def CreateGoodItem(self,ball):
        if len(self.GoodItemX) <self.Timer//1500 +1:
            self.GoodItemX.append(randint(50,250))
        if len(self.GoodItemY) <self.Timer//1500 +1:
            self.GoodItemY.append(randint(50,250))
        for i in range(0,len(self.GoodItemX)):
            self.Canvas.create_rectangle(self.GoodItemX[i], self.GoodItemY[i], self.GoodItemX[i]+10, self.GoodItemY[i]+10, fill="green")
        for i in range(0,len(self.GoodItemX)):
            if len(self.Canvas.find_overlapping(self.GoodItemX[i], self.GoodItemY[i], self.GoodItemX[i]+10, self.GoodItemY[i]+10)) is not 1:
                if ball in self.Canvas.find_overlapping(self.GoodItemX[i], self.GoodItemY[i], self.GoodItemX[i]+10, self.GoodItemY[i]+10):
                    self.Points+=100
                    self.Size+=0.5 
                    self.GoodItemX.pop(i)
                    self.GoodItemY.pop(i)
                    self.CreateGoodItem(ball)

#Subroutine for the bad item
    def CreateBadItem(self,ball):
        if len(self.BadItemX) <self.Timer//1500 +1:
            self.BadItemX.append(randint(50,250))
        if len(self.BadItemY) <self.Timer//1500 +1:
            self.BadItemY.append(randint(50,250))
        for i in range(0,len(self.BadItemX)):    
            self.Canvas.create_rectangle(self.BadItemX[i], self.BadItemY[i], self.BadItemX[i]+10, self.BadItemY[i]+10, fill="red")            
        for i in range(0,len(self.BadItemX)):
            if len(self.Canvas.find_overlapping(self.BadItemX[i], self.BadItemY[i], self.BadItemX[i]+10, self.BadItemY[i]+10)) is not 1:
                if ball in self.Canvas.find_overlapping(self.BadItemX[i], self.BadItemY[i], self.BadItemX[i]+10, self.BadItemY[i]+10):
                    self.Points-=50
                    self.Size-=0.5
                    self.BadItemX.pop(i)
                    self.BadItemY.pop(i)
                    self.CreateBadItem(ball)

#Subroutine for the power-up item
    def CreatePowerUpItem(self,ball):
        if len(self.BadItemY) is 0 or self.Timer%1000 == 0 :
            self.PowerUpItemX[0].append(randint(50,250))
            self.PowerUpItemY[0].append(randint(50,250))      
        for i in range(0,len(self.PowerUpItemX[0])):    
            self.Canvas.create_rectangle(self.PowerUpItemX[0][i], self.PowerUpItemY[0][i], self.PowerUpItemX[0][i]+10, self.PowerUpItemY[0][i]+10, fill="yellow")            
        for i in range(0,len(self.PowerUpItemX[0])):
            if len(self.Canvas.find_overlapping(self.PowerUpItemX[0][i], self.PowerUpItemY[0][i], self.PowerUpItemX[0][i]+10, self.PowerUpItemY[0][i]+10)) is not 1:
                if ball in self.Canvas.find_overlapping(self.PowerUpItemX[0][i], self.PowerUpItemY[0][i], self.PowerUpItemX[0][i]+10, self.PowerUpItemY[0][i]+10):
                    self.Points+=150
                    self.Size+=1
                    self.PowerUpItemX[0].pop(i)
                    self.PowerUpItemY[0].pop(i)
                    self.CreatePowerUpItem(ball)

#Subroutine for the circle sprite and the game over conditions            
    def paint(self):
        self.Canvas.delete(ALL)

        if self.Timer//100<=60:
            if 10*self.Size >0:
                ball=self.Canvas.create_oval(self.x-10*self.Size,self.y-10*self.Size,self.x+10*self.Size,self.y+10*self.Size, fill="white")
                self.CreateGoodItem(ball)
                self.CreateBadItem(ball)
                if randint(0,100)%2==0:
                        self.CreatePowerUpItem(ball)
            elif self.Size>=6:
                self.TimerText['text']="You win! :D"
                self.end()
            else:
                self.TimerText['text']="You lose! :("
                self.end()
        else:
            self.TimerText['text']="Time's up!"
            self.end()

#Subroutine for the wall collisions of the circle sprite       
    def MoveCircleSprite(self, b,speed):
        if self.UP==True and self.y-b>0:
            self.y-=speed
        elif self.UP==True and self.y-b<=0:
            self.UP=False
            self.DOWN=True
        if self.DOWN==True and self.y+b<300:
            self.y+=speed
        elif self.DOWN==True and self.y+b>=300:
            self.DOWN=False
            self.UP=True
        if self.LEFT==True and self.x-b>0:
            self.x-=speed
        elif self.LEFT==True and self.x-b<=0:
            self.LEFT=False
            self.RIGHT=True
        if self.RIGHT==True and self.x+b<300:
            self.x+=speed
        elif self.RIGHT==True and self.x+b>=300:
            self.RIGHT=False
            self.LEFT=True

#Subroutine to control the direction of movement of the circle sprite
#(through mouse clicks on the game canvas)
    def MouseClicks(self,event):
        self.tempx=event.x
        self.tempy=event.y
        if event.x> self.x and self.x is not self.tempx :
            self.RIGHT=True
            self.LEFT=False
        elif event.x< self.x and self.x is not self.tempx :
            self.LEFT=True
            self.RIGHT=False
        else:
            self.x=self.tempx    
            self.RIGHT=False
            self.LEFT=False
        if event.y> self.y and self.y is not self.tempy :
            self.DOWN=True
            self.UP=False
        elif event.y< self.y and self.y is not self.tempy :
            self.UP=True
            self.DOWN=False
        else:
            self.y=self.tempy
            self.DOWN=False
            self.UP=False
        

app=adventureCircle()        
