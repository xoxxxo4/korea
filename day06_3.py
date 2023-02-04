# 파일 읽고 쓰기

# 파일 만들고 쓰기(txt) : 이미 있으면 쓰기만
def 파일쓰기():
    f = open('sample.txt', 'w', encoding='UTF-8')
    f.write('안녕하세요 반갑습니다 감사합니다\n')       # \n : 엔터키, 한줄 바꾸기
    f.close()

# 파일 읽기(txt)

def 파일읽기():
    f = open('sample.txt', 'r', encoding='UTF-8')
    line = f.readline()         # 한 줄을 읽어옴
    print(line)

def 파일읽기():
    lines = f.readlines()       # 전체를 읽음
    print(lines)
    for line in lines:
        print(line, end='')
