from lib.shares import gulpShares
from pandas import DataFrame,read_csv

def getInvestment():
	shares = gulpShares()
	out = {}
	tot = 0
	h = {'nm':'', 'cost':0}
	l = {'nm':'', 'cost':999999}
	for share in shares:
		if len(shares[share]) == 0:
			continue
		s = 0
		u = 0

		for i in shares[share]:
			s += float(i)*shares[share][i]
			u += shares[share][i]
		out[share] = {'units': u, 'avg': (s/u), 'invested': s}
		h = {'nm':share , 'cost':float(max(shares[share]))} if float(max(shares[share])) >= h['cost'] else h
		l = {'nm':share , 'cost':float(min(shares[share]))} if float(min(shares[share])) < l['cost'] else l
		tot += s
	out['Overall'] = {'high_cost':h, 'low_cost':l, 'Total': tot}
	out['Division'] = getShareDivision(out)
	return out

def getShareDivision(inv):
	out = {}
	for i in [i for i in inv if '|' in i]:
		out[i] = round(inv[i]['invested'] * 100 / inv['Overall']['Total'], 2)
	out = {k: str(v)+' %' for k, v in sorted(out.items(), key=lambda item: item[1], reverse=True)}
	return out

def processProfitLoss():
	df_pl = read_csv("data/profitloss.csv")

	# print(df_pl)
	# print(df_pl.columns)
	df_profits = df_pl[df_pl['PROFIT/LOSS']=='PROFIT']
	df_loss = df_pl[df_pl['PROFIT/LOSS']=='LOSS']
	print(df_profits)
	print(df_loss)
