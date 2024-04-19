import turtle;

t = turtle.Pen()

t.pencolor("black")
command = input("왼쪽=left, 오른쪽=right, 종료=quit :")

while (1) :
    if(command == "left") :
        t.left(60)
        t.forward(50)
    elif(command == "right") :
        t.right(60)
        t.forward(50)
    elif(command == "quit") :
        break


turtle.done()