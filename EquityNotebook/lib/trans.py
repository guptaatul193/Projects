import os
import json
from datetime import datetime,date
from collections import defaultdict

tran_path = "data/trans.csv"

class Tran:
	def __init__(self,nm,mkt,units,idt,icost,sdt,scost):
		self.nm = nm
		self.mkt = mkt
		self.units = units
		self.idt = idt
		self.icost = icost
		self.sdt = sdt
		self.scost = scost

	def __str__(self):
		return str(self.__dict__)

def gulpTrans():
	with open(tran_path,'r') as f:
		trans = f.readlines()[1:]
	out = []
	for tran in [i.strip().split(',') for i in trans]:
		tran[3] = datetime.strptime(tran[3],"%Y-%m-%d")
		tran[5] = datetime.strptime(tran[5],"%Y-%m-%d")
		out.append( Tran(tran[0],tran[1],tran[2],tran[3],tran[4],tran[5],tran[6]) )
	return out

def refreshTrans( lst=[] ):
	with open(tran_path,'w') as f:
		f.write("SHARE_ID,UNITS,INVESTMENT_DATE,INVESTMENT_COST,SELLING_DATE,SELLING_COST\n")
		for i in lst:
			f.write("%s,%s,%s,%s,%s,%s\n" %(i.sid,i.units,datetime.strftime(i.idt,"%Y-%m-%d"),i.cost,datetime.strftime(i.sdt,"%Y-%m-%d"),i.scost))
