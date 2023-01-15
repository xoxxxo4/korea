# 파이썬 내장함수(제공기능)를 리스트에 응용

# len : 전체 갯수
# max : 최대값을 알려줌
# min : 최소값을 알려줌
# sum : 전체 합계

lst = [0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]

# lst. : lst의, 리스트 제공 함수

전체갯수 = len(lst)
최댓값 = max(lst)
최솟값 = min(lst)
전체합계 = sum(lst)
평균 = sum(lst)/len(lst)

print(전체갯수)
print(최댓값)
print(최솟값)
print(전체합계)
print(평균)