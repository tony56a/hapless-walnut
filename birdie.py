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
	def GET( self ):
		topic = None
		if( 'query' in web.input().keys() ):
			topic = web.input()[ 'query' ]
		returnValue = dbhandler.queryEntries( topic )
		if type( returnValue ) is str:
			return jsonrenderer.renderError( returnValue )
		else:
			return jsonrenderer.renderResponse( { 'topics': returnValue } )
	
class ModifyTopics:
	def POST( self, topicName ):		
		returnValue = dbhandler.addEntry( topicName ) 
		if returnValue is None:
			return jsonrenderer.renderResponse( { 'added': topicName } )
		else:
			return jsonrenderer.renderError( returnValue )

	def DELETE( self, topicName ):
		returnValue = dbhandler.removeEntry( topicName )
		if returnValue is None:
			return jsonrenderer.renderResponse( { 'deleted': topicName } )
		else:
			return jsonrenderer.renderError( returnValue )

class LoadTopics:
	def GET( self ):
		trendingTopics = webrequest.getTrendingTopics()
		if type( trendingTopics ) is str:
			return jsonrenderer.renderError( returnValue )
		else:
			numTopicsLoaded = 0
			for topic in trendingTopics:
				addEntryReturnValue = dbhandler.addEntry( topic[ 'name' ], topic[ 'url' ] ) 
				if addEntryReturnValue is None:
					numTopicsLoaded += 1
					
			return jsonrenderer.renderResponse( { 'numtopicsloaded': numTopicsLoaded } )

application = web.application(urls, locals())
