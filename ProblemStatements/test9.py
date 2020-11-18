from collections import defaultdict
n = defaultdict(dict)
for i in range(int(input())):
		n[i]['a'],n[i]['b'],n[i]['bound'] = map(int,input().split())

class ValueError(Exception):
	def __init__(self,a,b,bound):
		self.value = 'Multiplication of %d and %d is more than bound %d' %(a,b,bound)

	def __str__(self):
		return self.value

for i in n:
	try:
		if n[i]['a'] * n[i]['b'] > n[i]['bound']:
			raise ValueError(n[i]['a'],n[i]['b'],n[i]['bound'])
		print(n[i]['a'] * n[i]['b'])
	except ValueError as h:
		print( h )
