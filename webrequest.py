import conf
import web
import requests
from base64 import urlsafe_b64encode

def authorize():

	authUrl = 'https://api.twitter.com/oauth2/token'
	barerCred = conf.config['TwitterAPIKey']+':'+conf.config['TwitterAPISecret']
	headers = {
		'Content-Type' : 'application/x-www-form-urlencoded;charset=UTF-8',
		'Authorization' : 'Basic '+urlsafe_b64encode( barerCred )
	}
	data = 'grant_type=client_credentials'
	response = requests.post(authUrl, data=data, headers=headers)
	responseJson = response.json()
	if responseJson[ 'token_type' ] == 'bearer':
		return responseJson[ 'access_token' ]
	else:
		return None

def getTrendingTopics():
	returnValue = []
	requestUrl = 'https://api.twitter.com/1.1/trends/place.json'
	accessToken = authorize()
	if accessToken is not None:
		headers = {
		'Authorization' : 'Bearer '+ accessToken 
		}
		params = { 'id': 1}
		try:
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