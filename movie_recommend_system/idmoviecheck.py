import os		# operating system: eg.environment variables                    
import sys   # system utils: eg. std. input												
import json     # data format structures  
import time 	# proccess utils: time requests
import requests # http request: eg. get and post methods

from tmdb_movie_by_id import parametrize_api_connect

def get_movies_data(num_movies):

	cont=0
	_continue = True

	while _continue:

		status_code = parametrize_api_connect.get(cont).status_code
		
		time.sleep(0.5)
		cont+=1

		if status_code==404:
			print(cont,'movie_id not found')
		if cont==num_movies:
			_continue = False
	
def main():
	try:
		get_movies_data(sys.argv[1])
	except Error:
		print("you are forget something, maybe std imput:movie_id")
		
if __name__ == '__main__':
	main()
