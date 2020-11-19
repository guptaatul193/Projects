
pl_path = "data/profitloss.csv"
tran_path = "data/transactions.csv"

def logProfitLoss(dt,nm,mkt,inv_cost,sell_cost,units):
	pl = abs( inv_cost - sell_cost ) * units
	pl_percent = pl*100 / (inv_cost*units)
	typ = "PROFIT" if sell_cost > inv_cost else "LOSS"
	with open(pl_path,'a') as f:
		f.write("%s,%s,%s,%d,%.2f,%.2f,%s,%.2f,%.2f\n" %(dt,nm,mkt,units,inv_cost,sell_cost,typ,pl_percent,pl))

def logTransactions(typ,dt,nm,mkt,qty,cost):
	with open(tran_path, 'a') as f:
		f.write("%s,%s,%s,%s,%d,%.2f,%.2f\n" %(dt,typ,nm,mkt,cost,qty,(qty*cost)))
