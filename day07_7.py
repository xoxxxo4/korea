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

# 다른 사람이 '학생' 클래스 사용
# 클래스 업데이트 요청
