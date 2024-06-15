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

table = []

def init(table):
    for i in range(10):
        for j in range(10):
            if (i+j) % 2 == 1:
                table[i][j] = 1
                
    

for i in range(10):
    table += [[0] * 10]

init(table)

for i in range(10):
    print(table[i], end=" ")
    print()