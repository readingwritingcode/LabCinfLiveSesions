import os		# operating system: eg.environment variables                    
import system   # system utils: eg. std. input												
import json     # data format structures  
import time 	# proccess utils: time requests
import requests # http request: eg. get and post methods


'''Retrieve or collecte a bunch of movies data from TMDB.'''

def parametrize_api_connect(URL=True,API_KEY=True):
	
	API_KEY = os.environ['TMDB_API_KEY']

	tmdb_end_point = requests.Session()				# httpserver instance
	tmdb_end_point.params={'api_key':tmdb_api_key}			# httpSerever params
	
	return tmdb_end_point
	

def get_movie_data(movie_id):                                           # retrieve all metadata movie by id
	
	_url ='https://api.themoviedb.org/3/movie/{}'.format(movie_id)
	
	parametrize_api_connect()
	#make http request and handle api responses
	'''general form:
	try:
            response = tmdb_end_point.get(_url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            return "An Http Error occurred:" + repr(errh)
        except requests.exceptions.ConnectionError as errc:
            return "An Error Connecting to the API occurred:" + repr(errc)
        except requests.exceptions.Timeout as errt:
            return "A Timeout Error occurred:" + repr(errt)
        except requests.exceptions.RequestException as err:
            return "An Unknown Error occurred" + repr(err)
	
	search for common errors for get method and handle it!
	'''	
	# from response extract movie data
	
	dict_data = response.text
	
	return dict_data

def main():
	id = sys.argv[1]
	get_movie_data(id)

if __name__ == '__main__':
	main()
