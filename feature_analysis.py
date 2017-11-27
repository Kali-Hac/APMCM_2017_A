#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━  2017/11/24 14:54        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction： Used for feature analysis （Problem 2） √ ━━━━━☆*°☆*°
"""

from sklearn.linear_model import (LinearRegression, Ridge,
                                  Lasso, RandomizedLasso)
from sklearn.feature_selection import RFE, f_regression
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from minepy import MINE
import cPickle as pickle
all_info = []
class_dic = {}
ranks = {}
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
		label_data.append(class_dic[line[9]])
	print 'class_num：' + str(len(class_dic))
	return atr_data, label_data

def rank_to_dict(ranks, names, order=1):
	minmax = MinMaxScaler()
	ranks = minmax.fit_transform(order * np.array([ranks]).T).T[0]
	ranks = map(lambda x: round(x, 2), ranks)
	return dict(zip(names, ranks))


def run_feature_selection():
	X, Y = get_dataset()
	X = np.array(X)
	Y = np.array(Y)
	# print len(X[0])
	# names = ["x%s" % i for i in range(1, 8)]
	names = ['Age', 'Sex', 'Sleep quality', 'Sleep latency', 'Sleep time', 'Sleep efficiency', 'Sleep disorder',
	         'Hypnagogue', 'Daytime dyfunction']
	# names = ['Sex', 'Sleep quality', 'Sleep latency', 'Sleep time', 'Sleep efficiency', 'Sleep disorder', 'Hypnagogue', 'Daytime dyfunction']
	lr = LinearRegression(normalize=True)
	lr.fit(X, Y)
	ranks["Linear reg"] = rank_to_dict(np.abs(lr.coef_), names)

	ridge = Ridge(alpha=7)
	ridge.fit(X, Y)
	ranks["Ridge"] = rank_to_dict(np.abs(ridge.coef_), names)

	lasso = Lasso(alpha=.05)
	lasso.fit(X, Y)
	ranks["Lasso"] = rank_to_dict(np.abs(lasso.coef_), names)

	rlasso = RandomizedLasso(alpha=0.04)
	rlasso.fit(X, Y)
	ranks["Stability"] = rank_to_dict(np.abs(rlasso.scores_), names)

	# stop the search when 5 features are left (they will get equal scores)
	rfe = RFE(ridge, n_features_to_select=5)
	rfe.fit(X, Y)
	ranks["RFE"] = rank_to_dict(map(float, rfe.ranking_), names, order=-1)

	# rf = RandomForestRegressor()
	# rf.fit(X, Y)
	# ranks["RF"] = rank_to_dict(rf.feature_importances_, names)

	# f, pval = f_regression(X, Y, center=True)
	# # print len(f),len(names)
	# ranks["Corr."] = rank_to_dict(f, names)
	mine = MINE()
	mic_scores = []
	for i in range(X.shape[1]):
		mine.compute_score(X[:, i], Y)
		m = mine.mic()
		mic_scores.append(m)

	ranks["MIC"] = rank_to_dict(mic_scores, names)

	r = {}
	for name in names:
		r[name] = round(np.mean([ranks[method][name] for method in ranks.keys()]), 2)

	methods = sorted(ranks.keys())
	ranks["Mean"] = r
	methods.append("Mean")

	print ("\t%s" % "\t".join(methods))
	for name in names:
		print ("%s\t%s" % (name, "\t".join(map(str, [ranks[method][name] for method in methods]))))
	return ranks

if __name__ == '__main__':
	run_feature_selection()