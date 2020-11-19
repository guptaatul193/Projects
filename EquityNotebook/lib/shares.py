import os
import json
from collections import defaultdict
from datetime import datetime,date
from lib import trans

shares_path = "data/shares.json"

def gulpShares():
	try:
		with open(shares_path,'r') as f:
			shares = defaultdict(lambda:defaultdict(lambda:0),json.load(f))
	except:
		return defaultdict(lambda:defaultdict(lambda:0))
	return shares

def refreshSharesFile(shares):
	with open(shares_path,'w') as f:
		f.write(json.dumps(shares,indent=4))

def addShares( nm, mkt, cost, qty, dt ):
	if dt.lower() == 'today':
		dt = datetime.strftime(date.today(),'%Y-%m-%d')
	t = '%s|%s' %(nm,mkt)
	shares = gulpShares()
	if len(shares) == 0:
		shares[t][str(cost)] += qty
	else:
		shares[t] = defaultdict(lambda:0,shares[t])
		shares[t][str(cost)] += qty
	shares[t] = {i:shares[t][i] for i in sorted(shares[t])}
	refreshSharesFile( shares )
	trans.logTransactions('BUY',dt,nm,mkt,qty,cost)

def removeShares( nm, mkt, cost, qty, dt ):
	if dt.lower() == 'today':
		dt = datetime.strftime(date.today(),'%Y-%m-%d')
	t = '%s|%s' %(nm,mkt)
	shares = gulpShares()
	rm = {}
	if len(shares) == 0:
		return False
	elif qty > sum(shares[t].values()):
		return False
	else:
		for i in shares[t]:
			if shares[t][i] <= qty:
				rm[i] = shares[t][i]
				qty -= shares[t][i]
				shares[t][i] = 0
			if shares[t][i] > qty:
				rm[i] = qty
				shares[t][i] -= qty
				qty = 0
			if qty == 0:
				break
		shares[t] = {i:shares[t][i] for i in shares[t] if shares[t][i] != 0}
	refreshSharesFile(shares)
	for i in rm:
		trans.logTransactions('SELL',dt,nm,mkt,rm[i],float(cost))
		trans.logProfitLoss(dt,nm,mkt,float(i),float(cost),rm[i])
