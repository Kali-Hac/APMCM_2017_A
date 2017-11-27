#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━  2017/11/26 15:53        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：Use for drawing the most 4 diseases with sleeping quality √ ━━━━━☆*°☆*°
"""
import time
import cPickle as pickle
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot as plt
import numpy as np
all_info = []
class_dic = {}
# used for getting the training set X and labels(the kind of disease) y
def get_dataset():
	global all_info, class_dic
	save_file = open('Annex_II_dataset_all.pkl', 'rb')
	all_info = pickle.load(save_file)
	save_file.close()
	atr_datas = []
	label_data = []
	for line in all_info:
		atr_data = []
		atr_data.append(line[0])
		atr_data.extend([line[i] for i in range(2, 7)])
		atr_data.append(line[8])
		atr_datas.append(atr_data)
		if line[9] not in class_dic:
			class_dic[line[9]] = len(class_dic)
		label_data.append(class_dic[line[9]])
	print 'class_num：' + str(len(class_dic))
	return atr_datas, label_data

if __name__ == '__main__':
	x, y = get_dataset()
	names = class_dic.keys()
	# print names
	disease_num ={}
	for name, num in class_dic.items():
		if name not in disease_num:
			disease_num[name] = 0
			for label in y:
				if num == label:
					disease_num[name] += 1
	a = sorted(disease_num.items(), key=lambda d: d[1], reverse=True)
	t = []
	for name, num in a:
		if num > 30:
			t.append(class_dic[name])
	sleep_quality_0 = {}
	sleep_quality_1 = {}
	sleep_quality_2 = {}
	sleep_quality_3 = {}
	for k in range(len(x)):
		if x[k][1] == 0:
			if y[k] in t:
				i = y[k]
				if i not in sleep_quality_0:
					sleep_quality_0[i] = 0
				else:
					sleep_quality_0[i] += 1
		elif x[k][1] == 1:
			if y[k] in t:
				i = y[k]
				if i not in sleep_quality_1:
					sleep_quality_1[i] = 0
				else:
					sleep_quality_1[i] += 1
		elif x[k][1] == 2:
			if y[k] in t:
				i = y[k]
				if i not in sleep_quality_2:
					sleep_quality_2[i] = 1
				else:
					sleep_quality_2[i] += 1
		elif x[k][1] == 3:
			if y[k] in t:
				i = y[k]
				if i not in sleep_quality_3:
					sleep_quality_3[i] = 0
				else:
					sleep_quality_3[i] += 1
	Y_set = []
	for i in range(4):
		Y_set.append([])
	cnt = 0
	for i in t[4:8]:
		Y_set[cnt].append(sleep_quality_0[i])
		Y_set[cnt].append(sleep_quality_1[i])
		Y_set[cnt].append(sleep_quality_2[i])
		Y_set[cnt].append(sleep_quality_3[i])
		cnt += 1
	print Y_set
	plt.figure(figsize=(15, 6))
	n = 4
	X = np.arange(n)+1

	Y1 = np.array(Y_set[3])
	Y2 = np.array(Y_set[2])
	Y3 = np.array(Y_set[1])
	Y4 = np.array(Y_set[0])

	a = plt.bar(X, Y1, width=0.2, facecolor='lightskyblue', edgecolor='white')

	b = plt.bar(X+0.2, Y2, width=0.2, facecolor='yellowgreen', edgecolor='white')

	c = plt.bar(X + 0.4, Y3, width=0.2, facecolor='blue', edgecolor='white')

	d = plt.bar(X + 0.6, Y4, width=0.2, facecolor='red', edgecolor='white')

	plt.legend((a, b, c, d), (names[t[3]], names[t[2]], names[t[1]], names[t[0]]), loc='upper left')

	for x, y in zip(X, Y1):
		plt.text(x+0.1, y+0.05, y, ha='center', va='bottom')

	for x, y in zip(X, Y2):
		plt.text(x+0.25, y+0.05, y, ha='center', va='bottom')

	for x, y in zip(X, Y3):
		plt.text(x+0.5, y+0.05, y, ha='center', va='bottom')

	for x, y in zip(X, Y4):
		plt.text(x+0.75, y+0.05, y, ha='center', va='bottom')

	plt.xlabel('Sleep quality')
	plt.ylabel('Amount of people with different diagnosis')
	plt.xticks(range(1, 5), ['0', '1', '2', '3'])
	plt.ylim(0, +1000)
	plt.show()