# 입력 (변수가 필요)

변수 = input('입력할 문자열을 알려주세요 : ')
정수형 = int(input('입력할 정수를 알려주세요 : '))
print('내가 입력한 문자열 :',변수,'\n내가 입력한 정수형 :',정수형)    # \n : 줄 바꾸기


# 조건/반복문

if 정수형 < 10:
    print('10보다 작네요')
elif 정수형 < 100:
    print('100보다 작네요')
else:
    print('100 이상')

for i in range(5):
    print('5번 반복',i)

for i in lst:
    if i == 'hello':
        print('hello 찾음')
        break                  # 반복문을 즉시 종료
