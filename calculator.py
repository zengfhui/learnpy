#!/usr/bin/env python3

try:
	import sys
	salary = int(sys.argv[1])
	amount = salary - 3500
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

	print(format(tax,".2f"))
	
except:
 	print("Parameter Error")
 





 