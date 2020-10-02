import os		# operating system: eg.environment variables                    
import system   # system utils: eg. std. input												
import json     # data format structures  
import time 	# proccess utils: time requests
import requests # http request: eg. get and post methods


'''Retrieve or collecte a bunch of movies data from TMDB.'''


def get_movie_data(movie_id,tmdb_api_key = tmdb_api_key):
	
	URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
	tmdb_api_key = os.environ['TMDB_API_KEY']

	tmdb_api = requests.Session()				# python webserver instance
	tmdb_api.params={'api_key':tmdb_api_key}	# 

	url = URL.format(movie_id,tmdb_api_key)

	httpResp=tmdb_api.get(url)
	print(httpResp.status_code)
	global movie_json
	movie_json=httpResp.json()
	print(movie_json['success'])
	return movie_json

def main():
	continue_collecting = True

	id = 0
	while:
		'''Some id doesn't exists, hence response is 404. 
			Here, are catch the error. std.error. 
		'''
		try:
			pass
						# call api for some id. some id doesn't exists.
		except:
			pass


	#collect for a certain amount of time

	get_movie_data(sys.argv[1])

if __name__ == '__main__':
	main()