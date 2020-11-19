from lib.shares import gulpShares
from pandas import DataFrame,read_csv

def getInvestment():
	shares = gulpShares()
	out = {}
	tot = 0
	for share in shares:
		if len(shares[share]) == 0:
			continue
		s = 0
		for i in shares[share]:
			s += float(i)*shares[share][i]
		out[share] = s
		tot += s
	out['Total'] = tot
	return out

def processProfitLoss():
	df_pl = read_csv("data/profitloss.csv")
	# print(df_pl)
	# print(df_pl.columns)
	df_profits = df_pl[df_pl['PROFIT/LOSS']=='PROFIT']
	df_loss = df_pl[df_pl['PROFIT/LOSS']=='LOSS']
	print(df_profits)
	print(df_loss)
