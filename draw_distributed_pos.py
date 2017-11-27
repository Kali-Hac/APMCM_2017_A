#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━  2017/11/25 16:37        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：used for drawing the distribution chart √ ━━━━━☆*°☆*°
"""
import cPickle as pickle
from matplotlib import pyplot as plt
all_info = []
class_dic = {}
# used for getting the training set X and labels(the kind of disease) y
def get_dataset():
	global all_info, class_dic
	save_file = open('Annex_II_dataset_all.pkl', 'rb')
	all_info = pickle.load(save_file)
	save_file.close()
	atr_data = []
	label_data = []
	for line in all_info:
		if 'female' in line[1]:
			line[1] = 1
		else:
			line[1] = 0
		atr_data.append([line[j] for j in range(9)])
		# print [line[j] for j in range(9)]
		if line[9] not in class_dic:
			class_dic[line[9]] = len(class_dic)
			# print len(class_dic)
		label_data.append(class_dic[line[9]])
	print 'class_num：' + str(len(class_dic))
	return atr_data, label_data

if __name__ == '__main__':
	x, y = get_dataset()
	age = []
	age_y = []
	sex = []
	sex_y = []
	s_qua = []
	s_que_y = []
	# 睡眠相关
	s_y = []
	age_y.append(0)
	age.append(0)
	for i in range(len(x)):
		age_y.append(y[i])
		age.append(x[i][1] + 1)
	age_y.append(0)
	age.append(3)
	plt.xticks(range(1, 3), ['male', 'female'])
	# print age
	# for i in range(1, 15):
	# 	t = 0.2 * i
	# 	for j in range(len(age:
	# 		cnt = 0
	# 		if t - 0.05 < j < t + 0.05:
	#
	# 	print cnt
	# 	s_y.append(cnt)
	# r = [(0.2 * i) for i in range(1, 15)]
	# fig1 = plt.figure(2)
	# rects = plt.bar(left=tuple(r), height=tuple(s_y), width=0.2, align="center", yerr=0.000001)
	# plt.ylabel('Number of people')
	plt.ylabel("Diagnosis")
	plt.xlabel("Sex")
	plt.plot(age, age_y, 'ro', color='lightskyblue', label='Sleep quality')
	# plt.legend(loc='lower center', shadow=True, fontsize='x-large')
	plt.grid(True)
	plt.show()
	# cal_dic = {}
	# for i in range(len(x)):
	# 	t = age_y[i]
	# 	if t not in cal_dic:
	# 		cal_dic[t] = []
	# 		for j in range(len(x)):
	# 			if age_y[j] == t and age[j] not in cal_dic[t]:
	# 				cal_dic[t].append(int(age[j]))
	# 	else:
	# 		pass
	# age_dic= {}
	# for i in range(len(age)):
	# 	if age[i] not in age_dic:
	# 		age_dic[age[i]] = 1
	# b_name = class_dic.keys()
	# print len(age_dic)
	# for i in range(1, 6):
	# 	print str(i * 0.2)
	# 	for b_kind, ages in cal_dic.items():
	# 		if len(ages) > (0.2*i) * len(age_dic):
	# 			print b_name[b_kind], len(ages)

