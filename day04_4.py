# 문자열을 저장하는 리스트
lst = []

# 사용자에게 입력을 받아 리스트를 구성
# 1: 추가하기, 2: 수정하기, 3: 삭제하기, 4: 전체보기

while True:
    num = int(input('1: 추가, 2: 수정, 3: 삭제, 4: 조회, 0: 종료  '))
    if num == 1:
         lst.append(input('추가할 값을 입력하세요  '))
    elif num == 2:
        i = lst.index(input('수정하고자 하는 값을 입력하세요  '))
        lst[i] = (input('수정할 값을 입력하세요  '))
    elif num == 3:
        lst.remove(input('삭제할 값을 입력하세요  '))
    elif num == 4:
        print(lst)
    elif num == 0:
        print('프로그램을 종료합니다')
        break
    else:
        print('없는 번호입니다.')