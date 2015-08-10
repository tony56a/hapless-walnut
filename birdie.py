"""
Birdie sub-app, handles all Birdie REST calls
"""

import web
import jsonrenderer
import dbhandler
import webrequest

urls = (
	"/topics/load", "LoadTopics",
	"/topics", "AccessTopics",
	"/(.*)", "ModifyTopics"

)

class AccessTopics:
	"""
	Handler for querying topics
	"""
	def GET( self ):
		topic = None
		page = 0

		# If query topic name/page number are available, add them to query params
		if( 'query' in web.input().keys() ):
			topic = web.input()[ 'query' ]
		if( 'page' in web.input().keys() ):
			try:
				print web.input()['page']
				page = int( web.input()[ 'page' ] )
			except ValueError:
				# Return error for malformed page number values
				return web.badrequest()

		# Get a list of 10 topics matching topic name/all topics and page number
		returnValue = dbhandler.queryEntries( topic, page )

		# String responses indicate error, inform user
		if type( returnValue ) is str:
			return jsonrenderer.renderError( returnValue )
		else:
			return jsonrenderer.renderResponse( { 'topics': returnValue } )
	
class ModifyTopics:
	"""
	Handler for modifying the datastore
	"""

	def POST( self, topicName ):
		# Attempt to add topic to database  	
		returnValue = dbhandler.addEntry( topicName ) 
		if returnValue is None:
			return jsonrenderer.renderResponse( { 'added': topicName } )
		# Strings indicate an error, show user
		else:
			return jsonrenderer.renderError( returnValue )

	def DELETE( self, topicName ):

		# Attempt to remove entry from database
		returnValue = dbhandler.removeEntry( topicName )
		if returnValue is None:
			return jsonrenderer.renderResponse( { 'deleted': topicName } )
		# Strings indicate an error, show user
		else:
			return jsonrenderer.renderError( returnValue )

class LoadTopics:
	def GET( self ):
		# Get trending topics from Twitter 
		trendingTopics = webrequest.getTrendingTopics()
		# Strings indicate an error, show user
		if type( trendingTopics ) is str:
			return jsonrenderer.renderError( returnValue )
		else:
			# Attempt to add topics to db, keep track of successful adds
			numTopicsLoaded = 0
			for topic in trendingTopics:
				addEntryReturnValue = dbhandler.addEntry( topic[ 'name' ], topic[ 'url' ] ) 
				if addEntryReturnValue is None:
					numTopicsLoaded += 1

			# Return the number of topics added to user
			return jsonrenderer.renderResponse( { 'numtopicsloaded': numTopicsLoaded } )

application = web.application(urls, locals())
