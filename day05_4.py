# # 3개 더하기, 빼기, 곱하기, 나누기
# # +,-, *, / : 2 개만 할수 있음

# def 더하기(num1, num2, num3):
#     print(num1+num2+num3)

# print(1+2)
# 더하기(1, 2, 3)

# # 빼기, 곱하기, 나누기

# def 빼기(num1, num2, num3):
#     print(num1-num2-num3)
# def 곱하기(num1, num2, num3):
#     print(num1*num2*num3)
# def 나누기(num1, num2, num3):
#     print(num1/num2/num3)

# print(1+2)
# 더하기(1, 2, 3)
# 빼기(3, 2, 1)
# 곱하기(1, 2, 3)
# 나누기(10, 2 ,2)


# # return : 함수의 결과를 활용할 수 있게 해 줌

# def 절댓값더하기(a, b):
#     if a < 0:
#         a *= -1
#     if b < 0:
#         b *= -1
#     return(a+b)            # return 옆에 있는 값이 사용한 곳으로 전달
    
# 결과1 =절댓값더하기(3, 7)
# 결과2 = 절댓값더하기(-4, 결과1)
# print(결과2)
# print(절댓값더하기(-1,1))


# 문제1 : 리스트에 저장된 값의 총합을 구하는 함수를 만들고 return 값을 활용해 평균 구하기
lst = [10, 20, 30, 40, 50]
i = int(len(lst))

for i in range(i):
    print(lst[i])

def 총합(a_lst):
    s = a_lst[0] + a_lst[1] + a_lst[2] + a_lst[3] + a_lst[4]
    return s

sum = 총합(lst)
avg = int(sum/len(lst))

print('총합은',sum)
print('평균은',avg)

#문제2 : 입력한 갯수만큼 *을 표시하는 함수

def star(num):
    result = '*'
    for i in range(num):
        result += '*'
    return result

s1 = star(3)
s2 = star(5)
print(s1)