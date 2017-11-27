#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━  2017/11/25 23:19        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：Use for final classification for AnnexIII √ ━━━━━☆*°☆*°
"""
from sklearn import tree
import time
import cPickle as pickle
from sklearn.metrics import accuracy_score
from sklearn import metrics

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
	X, y = get_dataset()
	model = tree.DecisionTreeClassifier()
	start_time = time.time()
	M = model.fit(X, y)
	print('training took %fs!' % (time.time() - start_time))
	predicted = model.predict(X)
	expected = y
	print(metrics.classification_report(expected, predicted))
	print(metrics.confusion_matrix(expected, predicted))
	corre = accuracy_score(expected, predicted)
	print corre
	x = [[28,1,0,1,0,1,1],[37,2,1,2,1,2,0],[45,3,2,3,2,3,0],[32,3,3,3,0,2,2],[64,2,2,2,3,0,0], [29,3,2,2,0,1,1],[42,1,1,1,1,0,0],[36,1,3,3,2,1,1],[71,3,2,2,3,3,0], [26,1,2,3,2,1,1]]
	all_dis = []
	for t in class_dic.keys():
		all_dis.append(t)
	names = ['Age', 'Sleep quality', 'Sleep latency', 'Sleep time', 'Sleep efficiency', 'Sleep disorder','Daytime dyfunction']
	predicted = model.predict(x)
	for i in predicted:
		print all_dis[i]

