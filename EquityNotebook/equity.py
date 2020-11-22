from lib import shares,trans
from lib import summary as sm

# shares.buyShares('TATA','NSE',40.33,200,'today')
# shares.buyShares('TATA','NSE',43,300,'today')
# shares.buyShares('TATA','NSE',38,505,'today')
# shares.buyShares('TATA','BSE',41,10,'today')
# shares.buyShares('TATA','BSE',45,101,'today')
# shares.buyShares('MARUTI','BSE',412,100,'today')
# shares.buyShares('MARUTI','BSE',422,111,'today')
# shares.buyShares('MARUTI','BSE',427,100,'today')
# shares.buyShares('BEPL','NSE',82,1023,'today')
shares.buyShares('URJA','NSE',3.5,200,'today')
shares.buyShares('URJA','NSE',3.15,180,'today')

# shares.sellShares('MARUTI','BSE',100,300,'today')
# shares.sellShares('TATA','BSE',30,339,'today')
# shares.sellShares('TATA','BSE',57.5,100,'2020-11-25')
# shares.sellShares('TATA','BSE',49,400,'2020-11-30')
# shares.sellShares('TATA','NSE',48.7,123,'2020-11-30')

summary = sm.getInvestment()
for i in summary:
	print(i,summary[i] )

# summary.processProfitLoss()
