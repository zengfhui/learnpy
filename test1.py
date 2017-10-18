#!/usr/bin/env python3
'''
import sys
args = sys.argv[1:]
index = args.index('-c')
configfile = args[index+1]
index = args.index('-d')
datafile = args[index+1]
index = args.index('-o')
outputfile= args[index+1]

print(configfile)
print(datafile)
print(outputfile)
'''
class Config():
	def __init__(self,configfile):
		configfile = '/home/shiyanlou/c.cfg'
		with open(configfile) as file:
		self._config =dict()
		for line in file:
			tline = line.strip('\n')
			tmp = tline.split('=')
			self._config[tmp[0]] = float(tmp[1])
	
	def get_config(self):
		







filename2 = 'home/shiyanlou/d.txt'
with open(filename2) as file:
