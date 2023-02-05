# 변수 : 데이터를 저장하는 기술
# 함수 : 코드를 묶는 기술
# 클래스 : 변수와 함수를 묶는 기술

# 클래스 기반 프로그래밍 : 객체지향기법
# 클래스는 왜 만들었는가? 초보자한테 일을 시키려고
# 함수를 만들 능력이 없는 초보 개발자에게 기능을 제공 (단, 코드 교육은 안 함)

def AbsSum(n1, n2):
    result = 0
    if n1 < 0:
        n1 = n1 * -1
    if n2 < 0 :
        n2 + n2 * -1
    result = n1 + n2
    return result

# 초보 개발자는 변수를 만들어야 하고
# 함수를 적절히 사용해야 하고
# print 까지 해야 한다

result1 = AbsSum(-1, 3)
print(result1)

# 함수는 def, 클래스는 class
class 회사프로그램:
    n1 = 0            # 클래스 안에 있는 변수 : 멤버변수
    n2 = 0
    # 메서드 : 클래스 안에 있는 함수(매개변수 가장 앞에 self 라는 매개변수를 만들어놔야 함)
    def AbsSum(self, n1, n2):         # self : 메서드 고정 매개변수로, 사용하지 않음
        result = 0
        if n1 < 0:
            n1 = n1 * -1
        if n2 < 0 :
            n2 + n2 * -1
        self.n1 = n1                  # self.n1 : 매개변수의 n1
        self.n2 = n2                  # n2 : 지역변수의 n2
        result = n1 + n2
        return result
    def Last(self):                   # 사실상 매개변수가 없는 메서드(self)는 함수가 아니라 매서드라는 표시로 일단은 생각
        print(self.n1+self.n2)


# 객체화 : 클래스를 변수로 만든다

# 1. 클래스를 변수로 만든다
s = 회사프로그램()

# 2. s.AbsSum 을 사용한다. ()안에는 숫자 2개를, s에는 변수명을 적을 것
s.AbsSum(3, -5)

# 3 Last를 사용한다
s.Last()

# class == 변수와 함수를 묶는 기술 (세트 제품)