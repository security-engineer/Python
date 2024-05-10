str = "hell"
x = [10,20,30]


## 별 그리기 #######################

# count = int(input("별 몇줄? "))
# space_num = count
# star_num = 0
# for i in range(1,count+1) :
#     for j in range(1,space_num) :
#         print(" ", end="")
#     space_num = space_num - 1
#     for k in range(1, star_num+2) :
#         print("*", sep="", end="")
#     star_num = star_num + 1
#     print("")




## str 가운데 문자열 출력 ##################

# if((len(str) % 2) == 0) :
#     print(str[(len(str)//2)-1],str[(len(str)//2)], sep="", end="")
    
## for문 역순 ####################
# count = int(input("카운트 숫자 입력: ")) 
# for x in range (count, 0, -1) :
#     print(x, end=" ")
# print("발사")
    
    
## 정수 자릿수 더하기 ##############

num = int(input("정수: "))
sum = 0
num_count = 0
while(1) :
    if num // 10**num_count != 0 :
        num_count = num_count + 1
    else :
        break
    
    
for i in range(num_count, 0, -1) :
    sum += num // 10**(i-1)
    num = num % 10**(i-1)

print(sum)

