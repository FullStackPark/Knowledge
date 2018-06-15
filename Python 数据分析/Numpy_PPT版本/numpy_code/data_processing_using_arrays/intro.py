# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pylab

points = np.arange(-5, 5, 0.01) # 生成100个点
xs, ys = np.meshgrid(points, points)  # xs, ys互为转置矩阵
print xs
print ys
z = np.sqrt(xs ** 2 + ys ** 2)
print z
# 画图
plt.imshow(z, cmap = plt.cm.gray);
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
pylab.show() 