import random  #랜덤함수 호출

x = 10
a = 0
b13 = 0
b2= 0
c= 0

for i in range(x):  
  a = random.randint(1, 3)  #1학년 ~ 3학년 중에 랜덤으로 학년설정

  if a == 2:  #2학년인지 확인
    b2 = random.randint(1, 10)  #1반 ~ 10반 중에 랜덤으로 반설정
    c = random.randint(1, 35)  #1번 ~ 35번 중에 랜덤으로 번호설정
    print(str(a) + "학년 " + str(b2) + "반 " + str(c) + "번")
  else:
    b13 = random.randint(1, 9)  #1반 ~ 9반 중에 랜덤으로 반설정
    c = random.randint(1, 35)  #1번 ~ 35번 중에 랜덤으로 번호설정
    print(str(a) + "학년 " + str(b13) + "반 " + str(c) + "번")


  

