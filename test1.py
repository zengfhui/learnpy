#!/usr/bin/env python3

import sys
import json
'''
args = sys.argv[1:]
index = args.index('-c')
configfile = args[index+1]
index = args.index('-d')
userdatafile = args[index+1]
index = args.index('-o')
outputfile= args[index+1]
'''
configfile = '/home/shiyanlou/c.txt'
userdatafile = '/home/shiyanlou/d.txt'
outputfile = '/home/shiyanlou/o.txt'

class Config():
	def __init__(self,configfile):
		self._config =dict()
		with open(configfile) as file:
			for line in file:
				tline = line.strip('\n')
				tmp = tline.split('=')		# remebre rid of the kongge ,fouze wei 'JiShul ' er bu shi 'JisShuL'
				self._config[tmp[0]] = float(tmp[1])

#		try:
		self._JiShuL = self._config['JiShuL'] 
		self._JiShuH = self._config['JiShuH']
		tmp = 0
		for key,value in self._config.items():
			tmp = tmp + value
		self._rate = tmp - self._config['JiShuL'] - self._config['JiShuH']
#		except:
#			print("the configfile have the error")
	@property
	def get_JiShuL(self):
		return self._JiShuiL
	@property
	def get_JiShuH(self):
		return self._JiShuH
	@property
	def get_rate(self):
		return self._rate

class UserData():
	def __init__(self,userdatafile,Config):
		self._userdata = dict()
		with open(userdatafile) as file:
			count = 0
			for line in file:
				count += 1
				tline = line.strip('\n')
				tmp = tline.split(':')
				self._userdata[count] = [tmp[0],int(tmp[1])]
		self.number = count


#				tmp = ['100','1000']
#				d = dict()
#				d[1] = [tmp[0],int(tmp[1])]
#
#				print(d)
#				d = 1 : ['100',1000]
#
#				print(d[1][0])
#				'100'

	def caculator(self):

		rate = Config.get_rate	# 0.08 + 0.02 + 0.005 + 0.06 
		shebao = 0
		if salary < Config.get_JiShuL:
			shebao = 2193 * rate
		elif salary > Config.get_JiShuH:
			shebao = 16646 * rate
		else:
			shebao = salary * rate
		
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
		
	def dumpptofile(self,outputfile):
		sf = []
		stand ='0123456789.'
		for k in range(self.number):
			s = json.dumps(d[k])
			tmp = s.split(',')
			for i in range(len(tmp)):	
				for c in tmp[i]:
					if not c in stand:
						tmp[i] = tmp[i].replace(c,'')

			dit = ','
			sf[k] = dit.join(tmp)
		print(sf)

	def __getitem__(self,key):
		return self._userdata.get()
c = Config(configfile)
d = UserData(userdatafile,c)

d.dumpptofile(outputfile)









