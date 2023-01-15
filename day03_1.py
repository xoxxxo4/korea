횟수 = int(input('횟수를 입력하세요 >> '))
i = 0
while 1 < 횟수 :
    i += 1
    print (i, '번 째 Hello')


i = 1
while i < 101 :
    if i & 7 ==0:
        print(i)
    i += 1 


price = 300
금액 = int(input('금액이 얼마인가요 >> '))
커피잔수 = 0

while 금액 >= price:
    금액 -= price
    커피잔수 += 1
    print('커피',커피잔수,'잔, 잔돈',금액,'원')


 # 자료형 / 변수

'''
변수 : 저장공간
    - 대입연산자를 사용 =
    - 자주 변경될 것 같은, 혹은 자주 사용될 것 같은 값은 미리 저장해둬서 관리한다
    - 변수에 있는 값만 수정하면 변수를 사용한 코드는 일고라 수정이 가능
    - 변수명1 = '값'
    - 변수명 1 이라는 공간이 생성되면서(재활용되면서)'값' 이라는 데이터가 들어간다.


자료형(type) : 데이터의 타입
    - str, int, float
    - 오류검출, 실수검출, 의도명확화
    - 뺼셈으로 사용하고자 하는지, 핸드폰 번호롤 사용을 하고자 하는지 컴퓨터는 알 수 없음
    - 파이썬에서 제공해주는 기능(함수)를 잘못 사용했을 때 오류를 검출
    - str : 문자열(글자), int : 정수(숫자), float : 실수(소수점 있는 숫자)
    - 변수의 타입은 데이터의 타입과 일치해야만 저장이 가능
    - 자료형 변환
        1. '33-4'  ==>  int('33-4)  ==>  39
        2. 변환하고자 하는 자료형으로 감싸준다. float(정수변수)
        3. '문자열'  ==>  int('문자열')  ==>  컴파일 오류
        4. 데이터가 맞아야지만 타입 변형이 가능
'''

변수1 = 123
변수2 = '문자열'
int(변수1)
int(변수2)

# 변환하고자 하는 자료형과 호환가능한 값만 변환가능
# int(변수2) 
# 출력 / 입력

print('안녕')
print(3.14)
print(변수2)
print('안녕',변수2)
print('안녕 {}, {}, {}'.format(변수2, 변수1, 314))
print(f'안녕 {변수2}, {변수1}, {314}')

# 조건문 / 반복문

'''
if 조건식:
    조건식이 True 일때만 실행할 문장1
    조건식이 True 일때만 실행할 문장2

while 조건식:
    조건식이 True 일때만 실행할 문장1
    조건식이 True 일때만 실행할 문장2

조건문은 실행 후에 밑으로 내려가지만 반복문은 실행되면 위로(while 부분으로) 올라가서 조건식 검사부터 다시

'''


# if ~ elif ~ else

i = 3
if i == 3:
    print('조건이 맞네요')
    print('조건이 맞으면 이 문장은 실행이 됩니다')
print('조건문이 끝났습니다')

# while (반복문은 설계가 필요)
i = 0
while i < 3:
    print('반복문이 실행됩니다')
    print('조건이 맞는 동안에는 이 문장이 실행됩니다', i)
    i += 1
print('반복문이 끝났습니다')