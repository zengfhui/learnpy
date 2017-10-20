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

		try:
			self._JiShuL = self._config['JiShuL'] 
			self._JiShuH = self._config['JiShuH']
			tmp = 0
			for key,value in self._config.items():
				tmp = tmp + value
			self._rate = tmp - self._config['JiShuL'] - self._config['JiShuH']
			print(tmp)
			print(self._rate)
			print('36n')
		except:
			print("the configfile have the error")
	@property
	def get_JiShuL(self):
		return self._JiShuiL
	@property
	def get_JiShuH(self):
		return self._JiShuH

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

	def caculator(self,salary):

		rate = Config.get_rate()	 
		shebao = 0.0
		if salary < Config.get_JiShuL:
			shebao = 2193.0 * rate
		elif salary > Config.get_JiShuH:
			shebao = 16646.0* rate
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

		after_salary = salary - shebao - tax
		s = []
		s.append(shebao)
		s.append(tax)
		s.append(after_salary)
		return s
		
	def dumpptofile(self,outputfile):
		sf = []
		stand ='0123456789.'
		for k in range(self.number):
			s = json.dumps(self._userdata[k+1])
			tmp = s.split(',')
			for i in range(len(tmp)):	
				for c in tmp[i]:
					if not c in stand:
						tmp[i] = tmp[i].replace(c,'')

			dit = ','
			sf.append (dit.join(tmp))
		print(sf)

		with open(outputfile,'w') as file:
			for i in range(len(sf)):
				file.write(sf[i])
				#print(self._userdata[i+1][1]) 
				#print(type(self._userdata[i+1][1])) 
				salary = self._userdata[i+1][1]
				sf.extend(self.caculator(salary))
				#print(t)


			



c = Config(configfile)
d = UserData(userdatafile,c)

d.dumpptofile(outputfile)









