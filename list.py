# i = (int)(input("정수를 입력하세요: "))

# if (i % 2 == 0) :
#     print("입력한 정수는 짝수 입니다.")
#     print("sd")
# else :
#     print("입력한 정수는 홀수 입니다.")

#############################################################################################

# id = ["hong", "kim", "tae"]
# pw = 12345678
# input_id = input("아이디를 입력하세요: ")

# if (input_id in id) :
#     input_pw = (int)(input("패스워드를 입력하세요: "))    
#     if (pw == input_pw) :
#         print("환영합니다!")
#     else :
#         print("패스워드가 틀렸습니다.")
# else :
#     print("아이디가 틀렸습니다.")

###############################################################################################

# age = (int)(input("나이가 몇살 인가요? "));
# height = (int)(input("키는 몇인가요? "));

# if (age >= 10 & height >= 165):
#     print("탑승 가능!")
# else :
#     print("탑승 불가능!");

###############################################################################################

# 두 개의 정수를 입력 받아서 둘 중에서 큰 수를 출력하는 프로그램을 출력해봅시다.

# i = (int)(input("첫 번째 정수: "));
# j = (int)(input("두 번째 정수: "));

# if (i > j):
#     print("큰 수는 , i");
# else :
#     print("큰 수는", j);

################################################################################################

# price = (float)(input("구입 금액을 입력하세요: "));
# if (price >= 100000):
#     price = price * 0.95;
    
# print("지불 금액은 ", price, " 입니다.");

############################################################################################

# word = input("문자열 입력: ");
# length = len(word);

# if (length % 2 == 1) :
#     char1 = word[(int)(length/2)];
#     print("mid char: ", char1);
# else:
#     char2 = word[(int)(length/2)-1];
#     char3 = word[(int)(length/2)];
#     print("mid char: ", char2, char3);

################################################################################################

from random import randint

number = randint(1, 100);
count = 1;
while (1) :
    guess = (int)(input("숫자를 입력하시오: "));
    if(guess == number) :
        print("축하합니다! 시도횟수 = %d" %(count)); break;
    elif (guess < number) :
        print("높음!");
        count += 1;
    elif (guess > number) :
        print("낮음!");
        count += 1;
        


