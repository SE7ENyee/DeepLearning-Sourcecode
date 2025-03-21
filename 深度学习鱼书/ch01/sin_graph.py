# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
# 绘制图形
plt.plot(x, y1, linestyle="-.",label="sin")
plt.plot(x, y2, label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin&cos graph')
plt.legend(loc="best")
plt.show()
