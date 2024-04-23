quiz1 = int(input("첫번째 퀴즈 점수를 입력하세요: "))
quiz2 = int(input("두번째 퀴즈 점수를 입력하세요: "))
exam = int(input("시험 점수를 입력하세요: "))

total = quiz1 + quiz2 + exam

if exam < 30 or total < 60 :
    print("실패")
elif total >= 90 :
    print("탁월")
elif total >= 80 :
    print("우수")
else :
    print("양호")
    
    