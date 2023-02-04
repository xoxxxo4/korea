# 외부 함수를 사용하는 법 : import
# 모듈 : 무료

# import 모듈명
# import 모듈명 as 별명
# from 모듈명 import 함수명

import matplotlib.pyplot

lst = [10,20,12,31,41,90,66,11,44,88]
matplotlib.pyplot.hist(lst)
matplotlib.pyplot.show()

