"""
Methods for fetching trending topics
"""

import conf
import web
import requests
from base64 import urlsafe_b64encode

def authorize():
	"""
	Request access token for application using app API key
	"""
	authUrl = 'https://api.twitter.com/oauth2/token'

	# generate barer credentials
	barerCred = conf.config['twitterapikey']+':'+conf.config['twitterapisecret']

	# populate header and data according to Twitter docs
	headers = {
		'Content-Type' : 'application/x-www-form-urlencoded;charset=UTF-8',
		'Authorization' : 'Basic '+urlsafe_b64encode( barerCred )
	}
	data = 'grant_type=client_credentials'

	#request token, if granted, return that value
	response = requests.post(authUrl, data=data, headers=headers)
	responseJson = response.json()
	if responseJson[ 'token_type' ] == 'bearer':
		return responseJson[ 'access_token' ]
	else:
		return None

def getTrendingTopics( placeId=1 ):
	"""
	Request a list of top Twitter trends worldwide
	"""
	returnValue = []
	requestUrl = 'https://api.twitter.com/1.1/trends/place.json'

	#Authorize app
	accessToken = authorize()

	if accessToken is not None:

		# set header with access token
		headers = {
		'Authorization' : 'Bearer '+ accessToken 
		}
		# fill in required location field to fetch worldwide trending topics
		params = { 'id': placeId }
		try:
			# make request, and populate list to be returned with name and urls
			response = requests.get( requestUrl, params=params, headers=headers )
			responseJson = response.json()
			if 'trends' in responseJson[ 0 ]:
				for trend in responseJson[ 0 ][ 'trends' ]:
					returnValue.append( { 'name': trend[ 'name' ], 'url': trend[ 'url' ] } )
			return returnValue
		except HTTPError as e:
			web.debug( e )
	else:
		web.debug( "Failed to get Twitter values" )
		return "Error while fetching topics"