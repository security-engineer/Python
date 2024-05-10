# import turtle;

# t = turtle.Pen()

# t.pencolor("black")
# command = input("왼쪽=left, 오른쪽=right, 종료=quit :")

# while (1) :
#     if(command == "left") :
#         t.left(60)
#         t.forward(50)
#         command = input("왼쪽=left, 오른쪽=right, 종료=quit :")
#     elif(command == "right") :
#         t.right(60)
#         t.forward(50)
#         command = input("왼쪽=left, 오른쪽=right, 종료=quit :")
#     elif(command == "quit") :
#         break


# turtle.done()

# def get_sum (a,b) :
#     sum = 

# say_hello("철수","잘 지냈니!")

# str = input("문자열: ")
# alpha_num = 0
# digit_num = 0
# space_num = 0
# for i in str :
#     if(i.isalpha()) :
#         alpha_num += 1
#     if(i.isdigit()) :
#         digit_num += 1
#     if(i.isspace()) :
#         space_num += 1
        
# print(alpha_num, digit_num, space_num)

def FtoC(F) :
    return (F-32)*(5/9)
    
print(FtoC(100.0))