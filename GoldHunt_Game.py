#
# Cody Ball
# This program creates a game where the user attempts to find
#   5 gold circles a 15x15 grid of black circles. The user is given
#   5 rounds to play the game.
# Enhancement 1 - welcome / instruction window
# Enhancement 2 - Billy the Ball distraction level. Must click on the green ball addition
# Enhancement 3 - closing comment window
from graphics import*
from random import randint
import time
from time import sleep

def control():
     # create graphics window
     # create title rectangle with correct colors and text
     # create player text
     # draw everything
     win=GraphWin("Game Contol",250,200)
     titleR=Rectangle(Point(0,0),Point(250,40))
     titleR.draw(win)
     titleR.setFill("black")
     win.setBackground("light gray")
     titleT=Text(Point(125,20),"BOILER GOLD HUNT!")
     titleT.draw(win)
     titleT.setTextColor("gold")
     titleT.setStyle("bold")
     playerT=Text(Point(65,55),"PLAYER NAME")
     playerT.setStyle("bold")
     playerT.draw(win)
     entry1=Entry(Point(175,55),10)
     entry1.setFill("white")
     entry1.draw(win)

     # create TOP SCORES title
     topScores=Text(Point(125,90), "TOP SCORES")
     topScores.setStyle("bold")
     topScores.setSize(14)
     topScores.draw(win)

     # create NEW GAME box
     newR=Rectangle(Point(10,155),Point(110,190))
     newR.draw(win)
     newT=Text(Point(60,172), "NEW GAME")
     newT.setStyle("bold")
     newT.draw(win)
     newR.setFill("gold")
     # create EXIT box
     exitR=Rectangle(Point(240,190),Point(190,155))
     exitR.setFill("black")
     exitR.draw(win)
     exitT=Text(Point(215,172),"EXIT")
     exitT.setTextColor("white")
     exitT.setStyle("bold")
     exitT.draw(win)

     
     
     # return the new game box, exit box, and entry box
     return newR,exitR,win,entry1
# create a new function to create the game play window and text at top  
def goldhunt(name):
     # create new window with proper titles,set autoflush=False
     win2=GraphWin("GoldHunt",480,520,autoflush=False)
     headerR=Rectangle(Point(0,0),Point(480,40))
     headerR.setFill("black")
     headerR.draw(win2)
     roundT=Text(Point(50,20), "Round:")
     roundT.setTextColor("gold")
     roundT.draw(win2)
     clickT=Text(Point(430,20),"Clicks:")
     clickT.setTextColor("gold")
     clickT.draw(win2)
     # create entry text in the new window
     entryTP=Text(Point(240,20),"Player: "+name)
     entryTP.setTextColor("gold")
     entryTP.setStyle("bold")
     entryTP.draw(win2)
     
     # return win2, the round text,and click text
     return win2, roundT, clickT



# create a new function to create the list of circles and hidden
#    list of colors
def createCirc(win2):
     # create empty lists
    # hiddenC has colors
    # giantL has black circles
    hiddenC=[]
    giantL=[]
    # create list within lists
    for i in range(0,15):
        # formula to determine the center coordinates of each circle
        y=70+30*i
        # empty row list and hidden row list
        # we are doing two lists exactly the same because
        #      we want the hidden to be exactly alligned with the list of
        #      circles. This is so we can assign the color changes.
     
        row=[]
        hiddenR=[]
        # create the columns doing the same technique.
        for j in range(0,15):
            x=30*j+30
            circle=Circle(Point(x,y),15)
            circle.setFill("black")
            circle.draw(win2)
            row.append(circle)
            hiddenR.append('white')
        giantL.append(row)
        hiddenC.append(hiddenR)
        # find the random gold circle by generating a random row and random
        #      column assignment.
    randomrow=randint(0,14)
    randomcol=randint(0,14)

    # This is for red circle
    randomrowR=randint(0,14)
    randomcolR=randint(0,14)
    # this is for the green circle
    randomrowG=randint(0,14)
    randomcolG=randint(0,14)
    # Creates if statements if the red, green or gold ball line up with one
    #     another it will move them.
    if randomrowR == randomrow and randomcolR == randomcol:
         randomrow = randint(0,14)
         randomcol = randint(0,14)
    if randomrowG == randomrow and randomcolG == randomcol:
         randomrow = randint(0,14)
         randomcol = randint(0,14)
    if randomrowR == randomrowG and randomcolR == randomcolG:
         randomrowR = randint(0,14)
         randomcolR = randint(0,14)
         
    # when a randomrow or randomcol is =0, we are tired of finding the circle
    #     so we are setting it to the first position
    #randomrowR=0
    #randomcolR=0
    #randomrow = 0
    #randomcol = 0
    #randomrowG=0
    #randomcolG=0
   

    # for the grey circles, I want them 2 away from the gold.
    # create if statement to acccomodate if the randomrow-2=negative number
    #          (accounts for edge circles)
    for i in range(randomrow-2,randomrow+3):
        for j in range(randomcol-2,randomcol+3):
            if 0<=j<=14 and 0<=i<=14:
                 # allow this to occur only when i and j are inbetween 0&14
                hiddenC[i][j]='grey'
    for i in range(randomrow-1,randomrow+2):
         # do the same thing as grey for tan
        for j in range(randomcol-1,randomcol+2):
            if 0<=j<=14 and 0<=i<=14:
                hiddenC[i][j]='tan'
     # no arguments needed for gold,red, & green. just set it to the color
    hiddenC[randomrow][randomcol]='gold'
    hiddenC[randomrowR][randomcolR]='red'
    hiddenC[randomrowG][randomcolG]='green'
# return the proper things, hiddenC, giantL,circle
    return hiddenC,giantL,circle

# create new functionto create the rows and columns
# make this work with the clicks
def getRowCol(click,giantL):
    # get the coordinates of the click
    clickx=click.getX()
    clicky=click.getY()
    for i in range(0,15):
         # assign circles to row
       
        row=giantL[i]
       
        for j in range(0,15):
             # for each circle in row, get the center coordinates
             # we want function to work when clicked in circle
             # do distance formula so that the click is less than 15 away
             # if it is 15 away, yes!!
            circ=row[j]
           
            center=circ.getCenter()
            centerx=center.getX()
            centery=center.getY()
           
            distance=((clickx-centerx)**2+(clicky-centery)**2)**.5
            if distance<15:
                 #return i and j
                return i,j
# The bouncing ball needed for the shrinking circle function
# define the bouncing function that will be called later for shrinking circle
def bouncing(ball,dx,dy,r):         # Function 'bounces' ball off wall
    center=ball.getCenter()     # get center of ball
    if center.getX() not in range(4,460):   # within window (480,520)
        dx *= -1                            # change direction
        r -= 3
    if center.getY() not in range(38,500):
        dy *= -1
        r -= 3
    return dx,dy,r                            # return new values

# creating a function for the shrinking circle
# the shrink function needs to call the gold circle, and the GoldHunt window
def shrink(circles,win2):
    radius=15
    # set the ball equal to the gold circle
    ball=circles
    dx,dy = 3,-5                            # initial direction
    # Counting the clicks detected on the moving circle
    Clicks=0
    # Shrinking the circle
    while radius >= 0:
        ball.move(dx,dy)
        # calling the bouncing function
        dx,dy,radius = bouncing(ball,dx,dy,radius)
        c = ball.getCenter()
        x=c.getX()
        y=c.getY()
        sleep(0.02)
        ball.undraw()
        ball=Circle(Point(x,y),radius)
        ball.setFill("gold")
        ball.draw(win2)
        sleep(0.02)                         # sleep 0.02 seconds
        # detecting the clicks of the moving circle
        # if it detects a click, it will record the number of clicks
        # saved the clicks in the variable Clicks
        m=win2.checkMouse()
        if m != None:                   # Was there a mouse click?
            # The next line checks if the mouse click is within
            #  7 pixels of the center of the red box
            if abs(m.getX()-c.getX())<10 and abs(m.getY()-c.getY())<10:
                Clicks += 1             # Increase the mouse clicks
                #print(Clicks)
                                        # change movement direction
    ball.undraw()
    #show the ending message
    txt = Text(Point(249,260),"You win! Click to Play Again!")
    txt.draw(win2)
    # waiting for a click to start the next round of the game
    win2.getMouse()
    txt.undraw()
    return Clicks
# create main function
# call everything, but first control
def file():
    #put everything in def file so that you can call later
    #open the file
    # create open list to put scores in
    # read the file and get rid of new line thing and split at comma
    # make list of lists
     #then play game
   
    scoresList=[]
    ifile = open("scores.txt","r")
    data = ifile.readlines()
    ifile.close()
    for i in range(len(data)):
         # data[i] = 'Jd,5\n'
         info = data[i].strip('\n') # info = 'Jd,5'
         info = info.split(',') # info = ['Jd','5']
         scoresList.append([info[0],int(info[1])])
         # make the scoresList append the list of list so you can rank
   

     # do the if statements for length of data
     # we do if statements so it displays the proper scores for all lengths of data
     # including if the length is 0
    if len(data)>=3:          
         scoreOneName=scoresList[0][0]
         textOneN=Text(Point(100,110),scoreOneName)
         
         scoreOneScore=scoresList[0][1]
         textOneS=Text(Point(135,110),scoreOneScore)
         
         scoreTwoName=scoresList[1][0]
         textTwo=Text(Point(100,125),scoreTwoName)
       
         scoreTwo=scoresList[1][1]
         textTwoB=Text(Point(135,125), scoreTwo)
       
         scoreThreeName=scoresList[2][0]
         textThree=Text(Point(100,142),scoreThreeName)
         
         scoreThree=scoresList[2][1]
         textThreeB=Text(Point(135,142),scoreThree)
         
    if len(data)==2:
         scoreOneName=scoresList[0][0]
         textOneN=Text(Point(100,110),scoreOneName)
         
         scoreOneScore=scoresList[0][1]
         textOneS=Text(Point(135,110),scoreOneScore)
         
         scoreTwoName=scoresList[1][0]
         textTwo=Text(Point(100,125),scoreTwoName)
         
         scoreTwo=scoresList[1][1]
         textTwoB=Text(Point(135,125), scoreTwo)
         
         textThree=Text(Point(100,140),'')
         textThreeB=Text(Point(135,140),'')
     
    if len(data)==1:
         scoreOneName=scoresList[0][0]
         textOneN=Text(Point(100,110),scoreOneName)
         
         scoreOneScore=scoresList[0][1]
         textOneS=Text(Point(135,110),scoreOneScore)
         textTwo=Text(Point(100,125),'')
         textTwoB=Text(Point(135,125),'')
         textThree=Text(Point(100,140),'')
         textThreeB=Text(Point(135,140),'')
         
    if len(data)==0:
         textOneN=Text(Point(100,110),'')
         textOneS=Text(Point(135,110),'')
         textTwo=Text(Point(100,125),'')
         textTwoB=Text(Point(135,125), '')
         textThree=Text(Point(100,140),'')
         textThreeB=Text(Point(135,140),'')
         # set these equal to blank spaces so it returns something, these will
         #     be replaced later with set text later after 5 rounds have been played
    return textOneN,textOneS,textTwo,textTwoB,textThree,textThreeB,scoresList
# create checkControls so that if can be called and used for the green circle mini game
def checkControls(window):
     hop = window.getMouse()
     if hop.x<=40 and hop.y<=40:
          # return the spaces moved values
         return(-20,-20)
     elif hop.x>=210 and hop.y<=40:
         return(20,-20)
     elif hop.x<=40 and hop.y>=160:
         return(-20,20)
     elif hop.x>=210 and hop.y>=160:
         return(20,20)
     else:
         return(-1)
def main():
   
     
     #Put names in the game control        
    newR,exitR,win,entry1=control()
    # call file function and draw the texts at start of game              
    textOneN,textOneS,textTwo,textTwoB,textThree,textThreeB,scoresList=file()
    if len(scoresList)>=3:
         textOneN.draw(win)
         textOneS.draw(win)
         textTwo.draw(win)
         textTwoB.draw(win)
         textThree.draw(win)
         textThreeB.draw(win)
    if len(scoresList)==2:
         textOneN.draw(win)
         textOneS.draw(win)
         textTwo.draw(win)
         textTwoB.draw(win)
    if len(scoresList)==1:
         textOneN.draw(win)
         textOneS.draw(win)
    # gotta set the variables equal to something
    rounds=1
    clicks = 0
    name = "";
    # set these equal to none because its not time for their shinning moment yet
    win2 = None
    click2 = None
   
    # set up a while loop, make it equal to true because its gotta run
    #     only when true
    while True:
         # use get mouse so its constantly refreshing. Make it do work by saying
         #     when the argument is not equal to none, aka when you click
         #     thats when it is not equal to none
         click=win.checkMouse()
         if click != None:
              # print the entry name on top
              name = entry1.getText()
              # only function when name is not blank and the click is in the
              #     new game text box
              if name != "" and 10<click.x<110 and 130<click.y<180:
                   # now creating welcome window
                   # add titles and text, sleep(1) so that
                   #     text appears after previous text,
                   #     use sleep so it is more appealing and doesn't have text show all at once
                   #set to the right colors
                   win4=GraphWin("GET READY TO PLAY",400,200)
                   win4.setBackground("lightgray")
                   title4=Text(Point(200,30),"Welcome"+" "+name+"!")
                   title4.setStyle("bold")
                   title4.setSize(14)
                   title4.draw(win4)
                   sleep(1)
                   title42=Text(Point(200,50),"Are you ready to play?")
                   title42.draw(win4)
                   sleep(1)
                   title43=Text(Point(200,90),"Find the gold circle")
                   title43.draw(win4)
                   sleep(1)
                   title44=Text(Point(200,110),"in the least amount of clicks.")
                   title44.draw(win4)
                   sleep(1)
                   title45=Text(Point(200,130),"          adds 5 to your score.")
                   # include space so that red can be drawn separately and can be a different color
                   #     do the same with green
                   title455=Text(Point(125,130),"RED")
                   title455.setFill("red")
                   title455.draw(win4)
                   sleep(0.5)
                   title45.draw(win4)
                   sleep(1)
                   titleb=Text(Point(125,150),"GREEN")
                   titleb.setFill("green")
                   titleb.draw(win4)
                   sleep(0.5)
                   title46=Text(Point(200,150),"              starts a mini game.")
                   title46.draw(win4)
                   sleep(1)
                   titlec=Text(Point(200,175),"GOOD LUCK")
                   titlec.setStyle("bold")
                   titlec.draw(win4)
                               
                   # wait 3 seconds until the circles open
                   sleep(3)
                   win4.close()
         
                   # win2 should not equal none
                   if win2 != None:
                        win2.close()
                       
                    # open windows and lists    
                   win2,roundT,clickT=goldhunt(name)
                   hiddenC,giantL,circle=createCirc(win2)
         if(win2 != None):
              # set the texts to updated counts and clicks
               click2=win2.checkMouse()
               roundT.setText("Round: " + str(rounds))
               clickT.setText("Clicks: " + str(clicks))
         
         
   

         
         if click2 != None:
              # set things equal to variable
              buf = getRowCol(click2,giantL)
              if buf != None:
                   # add clicks and set the colors
                   # assign score to name and clicks
                   
                   clicks += 1
                   row,col= buf
                   color=hiddenC[row][col]
                   circles=giantL[row][col]
                   circles.setFill(color)
                   #score=[name,clicks]
                   #Set score =list with name and clicks  
                   # have it updated so it appears all at once
                   update(60)
                   if color=="red":
                        #if color is = red, clicks increases by 5, wrote 4 because when we put 5, it added 6
                        clicks+=4
                   if color == "green":
                        # wait a second to open window
                       sleep(0.5)
                       # create window for mini game with billy
                       # create rectangles, text, and set to proper colors
                       window = GraphWin("Hidden Game",250,200)
                       c1=Rectangle(Point(0,40),Point(40,0))
                       c2=Rectangle(Point(210,40),Point(249,0))
                       c3=Rectangle(Point(0,199), Point(40,160))
                       c4=Rectangle(Point(210,199),Point(249,160))
                       c1.draw(window)
                       c2.draw(window)
                       c3.draw(window)
                       c4.draw(window)
                       c1.setFill('gold')
                       c2.setFill('gold')
                       c3.setFill('gold')
                       c4.setFill('gold')
                       window.setBackground('black')
                       b=Circle(Point(125,100),12)
                       b.draw(window)
                       b.setFill('green')
                       gt = Text(Point(125,10),"Move Billy the ball")
                       gt2 = Text(Point(125,25),"4 times to close window")
                       gt.setTextColor('gold')
                       gt2.setTextColor('gold')
                       gt.draw(window)
                       gt2.draw(window)
                       # if in range 0-4, move the circle
                       for i in range(0,4):
                            if checkControls(window) != -1:
                                 dx,dy = checkControls(window)
                                 b.move(dx,dy)
                                 c = b.getCenter()
                       window.close()
               
                   if color == "gold":
                        # have it wait a second so not being done all at once
                        time.sleep(1)
                        # increase rounds
                        rounds+=1
                        #set background text
                        #message=Text(Point(240,260),"Congrats! Play Again")
                        #message.draw(win2)
                         # to make circles move:
                        for i in range(100):
                             for x in range(0,15):
                                  for y in range(0,15):
                                       if x!=row or y!= col:
                                            #exception for gold circle
                                            circ=giantL[x][y]
                                            circ.move(0,5)
                             time.sleep(0.005)
                             update(50)
                             # undraw things after the round so its fresh once gold circle is found
                        # calling the shrink circle function for the mini game
                        Clicks=shrink(circles,win2)
                        # To update, and get new clicks from the mini game
                        # The clicks collected in the mini game
                        # reduces the player's score by 2 points
                        clicks=((clicks-1)-(2*Clicks))
                        #circles.undraw()
                        #message.undraw()
                    # if rounds =6 close everything      
                        if rounds==6:
                             # start the closing window
                             # add text and proper colors
                             # draw and redraw so that the text appears to be getting larger
                             #     have it sleep so that the transition happens more smoothly
                             
                             win2.close()
                             win3=GraphWin("Game Contol",250,200)
                             win3.setBackground("cornsilk")
                             sleep(1)
                             title3=Text(Point(125,75), "GAME OVER")
                             title3.setSize(5)
                             title3.draw(win3)
                             sleep(0.01)
                             title3.undraw()
                             title3.setSize(6)
                             title3.draw(win3)
                             sleep(0.01)
                             title3.undraw()
                             title3.setSize(7)
                             title3.draw(win3)
                             sleep(0.01)
                             title3.undraw()
                             title3.setSize(8)
                             title3.draw(win3)
                             sleep(0.01)
                             title3.undraw()
                             title3.setSize(9)
                             title3.draw(win3)
                             sleep(0.01)
                             title3.undraw()
                             title3.setSize(10)
                             title3.draw(win3)
                             sleep(0.01)
                             title3.undraw()
                             title3.setSize(11)
                             title3.draw(win3)
                             sleep(0.01)
                             title3.undraw()
                             title3.setSize(12)
                             title3.draw(win3)
                             sleep(0.01)
                             title3.undraw()
                             title3.setSize(13)
                             title3.draw(win3)
                             sleep(0.01)
                             title3.undraw()
                             title3.setSize(14)
                             title3.draw(win3)
                             sleep(0.01)
                             title3.undraw()
                             title3.setSize(15)
                             title3.draw(win3)
                             sleep(0.01)
                             title3.undraw()
                             title3.setSize(16)
                             title3.draw(win3)
                             title3.setFill("darkolivegreen")
                             title3.setStyle("bold")
                             
                             sleep(1)

                             name3=Text(Point(125,100),name+"    "+"Your Score: "+str(clicks))
                             name3.setSize(5)
                             name3.draw(win3)
                             sleep(0.01)
                             name3.undraw()
                             name3.setSize(6)
                             name3.draw(win3)
                             sleep(0.01)
                             name3.undraw()
                             name3.setSize(7)
                             name3.draw(win3)
                             sleep(0.01)
                             name3.undraw()
                             name3.setSize(8)
                             name3.draw(win3)
                             sleep(0.01)
                             name3.undraw()
                             name3.setSize(9)
                             name3.draw(win3)
                             sleep(0.01)
                             name3.undraw()
                             name3.setSize(10)
                             name3.draw(win3)
                             sleep(0.01)
                             name3.undraw()
                             name3.setSize(11)
                             name3.draw(win3)
                             sleep(0.01)
                             name3.undraw()
                             name3.setSize(12)
                             name3.draw(win3)
                             sleep(0.01)
                             name3.undraw()
                             name3.setSize(13)
                             name3.draw(win3)
                             sleep(0.01)
                             name3.undraw()
                             name3.setSize(14)
                             name3.draw(win3)
                             sleep(0.01)
                             name3.undraw()
                             name3.setSize(15)
                             name3.draw(win3)
                             name3.setStyle("bold")
                             name3.setFill("goldenrod")
                             sleep(0.01)
                             # this determines what message is displayed based on number of clicks
                             # use an if statement to do that
                             if clicks>100:
                                  sorryText=Text(Point(125,125),"Woah! Score is a little high.")
                                  s2=Text(Point(125,140),"Try again next time!")
                                  sorryText.draw(win3)
                             if clicks<=100:
                                  congratsText=Text(Point(125,125),"Way to keep that score low!")
                                  congrats2=Text(Point(125,140),"Play Again!")
                                  congratsText.draw(win3)
                                  sleep(1)
                                  congrats2.draw(win3)
                              # sleep and have it close
                         
                         
                             sleep(4)
                             win3.close()
                             win2 = None
                             click2 = None
                             rounds = 1
                             score=[name,clicks]
                             clicks = 0
                             ##PUT THE TEXT DOCUMENT STUFF HERE
                             # sort the list in proper order
                             scoresList.append(score)
                             scoresList=sorted(scoresList,key=lambda x: x[1])
                             #print(scoresList)
                             # putting it into the txt file
                             ofile = open("scores.txt","w")
                             infoFirst = scoresList[0]
                             ofile.write(str(infoFirst[0])+','+str(infoFirst[1]))
                             for i in range(1,len(scoresList)):
                                  info=scoresList[i]
                                  ofile.write('\n'+info[0]+","+str(info[1]))
                             ofile.close()
                             # Redo the scores at top
                             # do this for if statements, draw the variables that have been
                             # added
                             # multiple if statements depending on length of scoresList so it draws proper amount
                             if len(scoresList)==3:
                                  textOneN.setText(scoresList[0][0])
                   
                                  textOneS.setText(scoresList[0][1])
                                 
                                  textTwo.setText(scoresList[1][0])
                                 
                                  textTwoB.setText(scoresList[1][1])
                                 
                                  textThree.setText(scoresList[2][0])
                                  textThree.draw(win)
                                  textThreeB.setText(scoresList[2][1])
                                  textThreeB.draw(win)
                             if len(scoresList)>3:
                                 
                                  textOneN.setText(scoresList[0][0])
                   
                                  textOneS.setText(scoresList[0][1])
                                 
                                  textTwo.setText(scoresList[1][0])
                                 
                                  textTwoB.setText(scoresList[1][1])
                                 
                                  textThree.setText(scoresList[2][0])
                                 
                                 
                                  textThreeB.setText(scoresList[2][1])
                                 
                                 
                             if len(scoresList)==2:
                                  textOneN.setText(scoresList[0][0])
                                 
                                  textOneS.setText(scoresList[0][1])
                                 
                                  textTwo.setText(scoresList[1][0])
                                  textTwo.draw(win)
                                 
                                  textTwoB.setText(scoresList[1][1])
                                  textTwoB.draw(win)
                                 
                                 
                             if len(scoresList)==1:
                                  textOneN.setText(scoresList[0][0])
                                 
                                  textOneS.setText(scoresList[0][1])
                                  #print(scoresList[0][1])
                                 
                                  textOneN.draw(win)
                                  textOneS.draw(win)
                             
                        else:
                             # this makes it repeat
                              hiddenC,giantL,circle=createCirc(win2)
                             
                             
           # if we click exit box, close everything  
         elif click != None and 190<click.x<240 and 130<click.y<180:
               
               win.close()
               if win2 != None:
                    win2.close()
               break
         update(60)
                         
# close the function

               
main()
