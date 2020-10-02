import os		# operating system: eg.environment variables                    
import sys   # system utils: eg. std. input												
import json     # data format structures  
import time 	# proccess utils: time requests
import requests # http request: eg. get and post methods


'''Retrieve or collecte a bunch of movies data from TMDB.'''


def get_movie_data(movie_id):
	
	URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
	tmdb_api_key = os.environ['TMDB_API_KEY']

	tmdb_api = requests.Session()				# python webserver instance
	tmdb_api.params={'api_key':tmdb_api_key}	# load info instance

	url = URL.format(movie_id,tmdb_api_key)

	httpResp=tmdb_api.get(url)
	global status_code
	status_code = httpResp.status_code
	return status_code

def get_movies_data(num_movies):

	cont=0
	_continue = True

	while _continue:

		get_movie_data(cont)
		
		time.sleep(0.5)
		cont+=1

		if status_code==404:
			print(cont,'movie_id not found')
		if cont==num_movies:
			_continue = False
	

def main():
	get_movies_data(sys.argv[1])

if __name__ == '__main__':
	main()