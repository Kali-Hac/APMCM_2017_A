#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━  2017/11/25 15:20        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：        √ ━━━━━☆*°☆*°
"""
import feature_analysis as data
import numpy as np
from matplotlib import pyplot as plt
if __name__ == '__main__':
	ranks = data.run_feature_selection()
	print ranks
	Y_set = []
	value = ranks["Linear reg"]
	temp = []
	for key, val in value.items():
		temp.append(val)
	Y_set.append(temp)
	# print Y_set
	value = ranks["Mean"]

	temp = []
	for key, val in value.items():
		temp.append(val)
	Y_set.append(temp)
	value = ranks["Stability"]

	temp = []
	for key, val in value.items():
		temp.append(val)
	Y_set.append(temp)
	plt.figure(figsize=(15, 6))
	n = 9
	X = np.arange(n)+1

	Y1 = np.array(Y_set[0])
	Y2 = np.array(Y_set[1])
	Y3 = np.array(Y_set[2])
	a = plt.bar(X, Y1, width=0.25, facecolor='lightskyblue', edgecolor='white')

	b = plt.bar(X+0.25, Y2, width=0.25, facecolor='yellowgreen', edgecolor='white')

	c = plt.bar(X + 0.5, Y3, width=0.25, facecolor='blue', edgecolor='white')

	plt.legend((a, b, c,), (u"Linear reg", u"Mean", u"Stability",))

	for x, y in zip(X, Y1):
		plt.text(x+0.1, y+0.05, '%.2f' % y, ha='center', va='bottom')

	for x, y in zip(X, Y2):
		plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va='bottom')

	for x, y in zip(X, Y3):
		plt.text(x+0.7, y+0.05, '%.2f' % y, ha='center', va='bottom')
	plt.ylim(0, +1.25)
	plt.show()

