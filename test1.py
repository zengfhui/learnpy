#!/usr/bin/env python3
'''
import sys
args = sys.argv[1:]
index = args.index('-c')
configfile = args[index+1]
index = args.index('-d')
useratafile = args[index+1]
index = args.index('-o')
outputfile= args[index+1]

'''
class caculator():
	def __init__(self,salary)
		self.salaty = salary
	def shebao(self):
		

	rate = 0.165	# 0.08 + 0.02 + 0.005 + 0.06 
	amount = salary * (1 - rate) - 3500
	tax = 0
	#tax = 0 is impotant! if loss, 
	# will raise erroe when salary > 5000 (amount >0))
	if amount < 0:
	 	tax = 0
	elif amount < 1500:
	 	tax = amount * 0.03
	elif tax < 4500:
	 	tax = (amount * 0.1) - 105
	elif amount < 9000:
	 	tax = (amount * 0.2) - 555
	elif amount < 35000:
	 	tax = (amount * 0.25) - 1005
	elif amount < 55000:
	 	tax =  (amount * 0.3) - 2755
	elif amount < 80000:
	 	tax = (amount * 0.35) - 5505
	else:
	 	tax = (amount * 0.450) -13505

	return salary*(1 - rate) - tax

class Config():
	def __init__(self,configfile):
		configfile = '/home/shiyanlou/c.cfg'
		self._config =dict()
		with open(configfile) as file:
			for line in file:
				tline = line.strip('\n')
				tmp = tline.split('=')
				self._config[tmp[0]] = float(tmp[1])
		try:
			self._JiShuL = self._config['JiShuL'] 
			self._JiShuH = slef._config['JiShuH']
			tmp = 0
			for key,value in self._config.items():
				tmp = tmp + value
			self._rate = tmp - self._config['JiShuL'] - self._config['JiShuH']
		except:
			print("the configfile have the error")

	def get_JiShuL(self):
		return self._JiShuiL
	def get_JiShuH(self):
		return self._JiShuH
	def get_rate(self):
		return self._rate

class UserData():
	def __init__(self,userdatafile):
		self._userdata = dict()
		wiht open(userdatafile) as file:
			count = 0
			for line in file:
				count += 1
				tline = line.strip('\n')
				tmp = tline.split(',')
				self._userdata[count] = [tmp[0],int(tmp[1])]


'''
				tmp = ['100','1000']
				d = dict()
				d[1] = [tmp[0],int(tmp[1])]

				print(d)
				d = 1 : ['100',1000]

				print(d[1][0])
				'100'
'''


	def get_shebao(self,number):
		salary =self._userdata[number] [1]
		caculator.(salary)	


filename2 = 'home/shiyanlou/d.txt'
with open(filename2) as file:
'''





