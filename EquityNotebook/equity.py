from lib import shares,trans
from lib import summary as sm
from flask import Flask,jsonify,render_template


app = Flask(__name__,template_folder='web')

@app.route('/')
def getinv():
	return jsonify(sm.getInvestment())

@app.route('/home', methods = ['GET'])
def gethome():
	return render_template("html/home.html")

# shares.buyShares('URJA','NSE',3.5,200,'today')
# shares.buyShares('URJA','NSE',3.15,180,'today')

# shares.sellShares('MARUTI','BSE',100,300,'today')
# shares.sellShares('TATA','BSE',30,339,'today')


# summary = sm.getInvestment()
# for i in summary:
# 	print(i,summary[i] )

# summary.processProfitLoss()

if __name__ == '__main__':
	app.run(debug = True)
