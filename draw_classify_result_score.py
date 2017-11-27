#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━  2017/11/25 21:37        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：        √ ━━━━━☆*°☆*°
"""
import matplotlib.pyplot as plt #引入matplotlib的pyplot子库，用于画简单的2D图
import random
import cPickle as pickle
names = ['Age', 'Sleep quality', 'Sleep latency', 'Sleep time', 'Sleep efficiency', 'Sleep disorder',
		'Daytime dyfunction']
f = open('model_result.pkl', 'rb')
all_info = pickle.load(f)
f.close()
methods = []
result = []
feature = []
for i in range(34, 37):
	methods.append(all_info[i][2])
	result.append(all_info[i][1])
	feature.append(all_info[i][0])
name_str = 'Accuracy rate with different extraction features '
# for i in feature[0]:
# 	name_str += names[i] + '/'
# print name_str
x = range(len(methods))
#建立对象

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
ax.set_title(name_str)
plt.xticks(range(len(methods)), methods)
for i in range(1, len(result)):
	strs = '('
	for j in range(len(feature[i])):
		if not j == 0:
			strs += '/' + str(feature[i][j])
		else:
			strs += str(feature[i][j])
	strs += ')'
	plt.annotate((' %.3f' % result[i] + '\n' + strs), xy=(i, result[i]))
plt.xlabel('Classification method')
plt.ylabel('Accuracy rate')
plt.plot(x, result, 'o-', label=u"线条")    #画图
plt.grid()
plt.show()