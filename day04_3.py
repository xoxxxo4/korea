cafe_menu = []

# 카페 메뉴 이름

cafe_menu.append('아메리카노')
cafe_menu.append('카페라떼')
cafe_menu.append('카푸치노')
cafe_menu.append('카라멜마끼아또')

print(cafe_menu)
print(cafe_menu[0])

for i in cafe_menu:
    print(i)

# 데이터의 갯수 len
리스트의갯수 = len(cafe_menu)
print(리스트의갯수)


# 수정
cafe_menu[0] = '에스프레소'

