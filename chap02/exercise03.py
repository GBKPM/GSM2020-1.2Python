# c연습문제3> Up & Down 게임 만들기
import random

#정답 만들기

jungdap = 0
count =0
print('1~100 사이의 랜덤 숫자 맞추기 게임')
while True:
    count += 1
    user_input = int(input(f'{count}숫자를 입력하세요: '))
    if jungdap == user_input:
        break
    elif jungdap > user_input:
        print(f'{user_input}보다')