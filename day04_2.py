# 리스트 = [ ]
# 리스트 : 변수들을 뭉쳐놓은 것

a = 1
b = 2
c = 3
d = 4

abcd = [1,2,3,4]

print(abcd)

for i in abcd:
    print(i)


# 3이 저장되어있는 방번호를 찾아보자
result = abcd.index(1)
print('해당 데이터가 저장되어 있는 위치는 : ',result)


# 리스트에 저장된 값들 중 하나만 사용하고자 한다면
print(abcd[2])


# 리스트 뒤에 추가 append
abcd.append(314)

print(abcd)


# 중간에 삽입 insert (나머지는 뒤로 밀어버림)
abcd.insert(2, 2222)

print(abcd)


# 수정
abcd[4] = 567


# 제거 remove
abcd.remove(2222)
print(abcd)


# 뒤쪽부터 뽑기 pop
뽑기결과 = abcd.pop()
print(abcd)
print(뽑기결과)


# 리스트 비우기 clear
abcd.clear()
print(abcd)


# 리스트 합치기 extend
abcd2 = [1,2,3,4,5,6,7,8,9,10]
abcd.extend(abcd2)
print(abcd)


#리스트 뒤집기 reverse
abcd.reverse()
print(abcd)


# count
십의갯수 = abcd.count(10)
print(십의갯수)


# 리스트 정렬 sort (기본적으로 낮은 순부터 오름차순으로 정렬)
abcd.sort()
print(abcd)


# 현재 리스트를 보존하면서 테스트를 하고 싶다
test_abcd = abcd.copy()
print('기존 리스트를 보존하면서 복붙을 만듭니다 :',test_abcd)


# 특정 데이터의 갯수 len