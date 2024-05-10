
a = 3
b = 3000

num = 123
str_num = str(num)

i = 0
sum = 0;
while(i < len(str_num)) :
    sum += int(str_num[i])
    i = i + 1

print(sum)


# print("사과", a, "개의 가격은", b ,"이다.")
# print(f"사과 {a}개의 가격은 {b}이다.")