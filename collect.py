#read structured user-query.

#call api. api params = values user query.

#process api results with user criteria.

#store results

##example of codes
''' Write 1000 liness of text data in .txt file.
'''
import time

_continue=True
ciclo=0
time_start=time.time()
cont = 1
while _continue:

	with open('datacollected.txt','a') as data_handled:

		data='ciclo %s' % ciclo
		ciclo+=1

		data_handled.write(ciclo*'IlovePython'+'\n')
		#print(ciclo,'write')
		print(ciclo*'*')

	time.sleep(0.1)
	print('write',cont,'de', 10000)
	cont+=1

	if cont == 10001:
		_continue=False
