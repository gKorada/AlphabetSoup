import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":#Goutham's 5
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":#Carter's 5
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":#Gabe's5
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":#Nick's 5
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(25)
        tur.left(90)
        tur.fd(25)
        tur.right(45)
        tur.fd(10)
        tur.right(180)
        tur.fd(20)
        tur.right(180)
        tur.fd(10)
        tur.left(135)
        tur.fd(25)
        tur.left(90)
        tur.fd(25)
        tur.right(180)
        tur.pu()
        tur.fd(55)
        tur.left(90)
        tur.fd(5)
        tur.right(90)
    elif letter == "R":
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(15)
        tur.left(135)
        tur.fd(20)
        tur.pu()
        tur.left(135)
        tur.fd(35)
        tur.right(90)
        tur.fd(25)
    elif letter == "S":
        tur.pu()
        tur.fd(35)
        tur.right(90)
        tur.fd(5)
        tur.right(90)
        tur.pd()
        tur.fd(30)
        tur.left(90)
        tur.fd(15)
        tur.left(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(30)
        tur.pu()
        tur.right(90)
        tur.fd(35)
        tur.right(90)
        tur.fd(35)

    elif letter == "T":
         tur.pu()
         tur.fd(5)
         tur.right(90)
         tur.fd(5)
         tur.left(90)
         tur.pd()
         tur.fd(30)
         tur.right(180)
         tur.fd(15)
         tur.left(90)
         tur.fd(30)
         tur.pu()
         tur.left(180)
         tur.fd(35)
         tur.right(90)
         tur.fd(20)
         
    elif letter == "U":
         tur.fd(10)
         tur.right(90)
         tur.fd(5)
         tur.pd()
         tur.fd(30)
         tur.left(90)
         tur.fd(20)
         tur.left(90)
         tur.fd(30)
         tur.pu()
         tur.fd(5)
         tur.right(90)
         tur.fd(10)
         
    elif letter == "V":#Chase does last 5
	    pass
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	
2






window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
#turtleLetter("box",tur)
turtleLetter("A",tur)


window.exitonclick()
