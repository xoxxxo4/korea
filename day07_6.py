# 속성 : 이름, 번호, 키
# 학생 클래스
# 기능(메서드) : 학생정보보기, 학생정보입력, __init__

class 학생:
    이름 = ''
    번호 = 0
    키 = 0.0
    def 학생정보보기(self):
        print(self.이름, self.번호, self.키)
    def __init__(self, a, b, c):
        self.이름 = a
        self.번호 = b
        self.키 = c
    def 학생정보입력(self, a, b, c):
        self.이름 = a
        self.번호 = b
        self.키 = c


철수 = 학생('김철수', 1, 177.7)
영희 = 학생('박영희', 2, 155.5)
짱구 = 학생('신짱구', 3, 173.3)

철수.학생정보보기()
영희.학생정보보기()
짱구.학생정보보기()

짱구.학생정보입력('짱구', 4, 174.8)
짱구.학생정보보기()