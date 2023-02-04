# pip install scikit-learn


# 머신러닝 모듈
import sklearn

# 그래프 모듈
import matplotlib.pyplot

# 수학/과학 계산 모듈
import numpy as np

# 다차원 데이터 모듈
import pandas as pd


print(sklearn.__version__)


'''
머신러닝 : 데이터(정제) -->  기계학습  -->  예측결과  -->  머신러닝별 비교 후 선정 
'''

# 데이터를 가져온다 csv
원본데이터 = pd.read_csv('sample.csv', encoding='UTf-8')
print(원본데이터.head())        # 잘 가져왔는지 상위 5개만 보기

# x(원인), y(결과)
x = 원본데이터.iloc[:,:-1].values
y = 원본데이터.iloc[:,-1].values
print(x)
print(y)

