import turtle
from turtle import Screen

#Establish Screen and Turtle
screen = Screen()
pen = turtle.Turtle()
pen.speed(-1)    #Set turtle speed to fastest
pen.width(5)    #Set turtle width to 5 for wider line

#Main Function
def main():
    #Sub-Function to move pen when left mouse clicked on screen
    def pen_move(x, y):
        pen.penup()    #lifts pen up off screen, no draw
        pen.goto(x, y)    #move to x,y coordinate of mouse when clicked
        pen.pendown()    #put pen back down on screen
    #Sub-Function for making a line
    def pen_draw(x, y):
        pen.ondrag(None)    #no input until heading set
        pen.setheading(pen.towards(x, y))    #heading set
        pen.goto(x, y)    #pen goes to x, y as moved
        pen.ondrag(pen_draw)    #function is recusrive to repeat as long as pen is dragged

    def pen_clear(x, y):
        pen.clear()    #screen cleared

    def one():
        pen.color("black")    #Color change 1

    def two():
        pen.color("red")    #Color change 2

    def three():
        pen.color("orange")    #Color change 3

    def four():
        pen.color("green")    #Color change 4

    #Instructions printed on screen when first initialised
    pen.write("    Instructions: 1 Black, 2 Red, 3 Orange, 4 Green.", font=("Arial", 12, "normal"))
    pen.goto(0, -20)    #Coord for second line of instructions
    pen.write("    Left click to move turtle and hold to draw,", font=("Arial", 12, "normal"))
    pen.goto(0, -40)    #Coord for third line of indstructions
    pen.write("    Right click to clear all", font=("Arial", 12, "normal"))


    pen.ondrag(pen_draw)    #When pen/turtle dragged, run pen_draw function
    turtle.onscreenclick(pen_move, 1)     #Run move_pen function
    turtle.onscreenclick(pen_clear, 3)    #Run pen_clear function
    #Color change functions
    turtle.onkey(one, '1')
    turtle.onkey(two, '2')
    turtle.onkey(three, '3')
    turtle.onkey(four, '4')


    turtle.listen()    #listen for input
    screen.mainloop()    #screen loop finalised
main()    #main function finalised

pen.listen()    #listen for input
pen.mainloop()    #finalise main loop
