# 무작위의 수를 생성
import random
# 순차적인 수를 생성
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
# animation 효과, 실시간 데이터 반영
from matplotlib.animation import FuncAnimation
 
plt.style.use('fivethirtyeight')
 
x_val = []
y_val = []
 
# 순차적인 수를 생성 
index = count()
 
def animate(i):
    x_val.append(next(index))
    # 0~10 사이의 랜덤한 정수 생성
    y_val.append(random.randint(80,100))
    # 앞선 그래프를 삭제
    plt.cla()
    plt.plot(x_val, y_val)

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
# plt.gcf(): 현재 그래프 모양을 가져옴
# animate: 애니메이션 효과 적용
# interval = 1000: 1000 밀리초마다 적용
 
plt.tight_layout()
plt.show()