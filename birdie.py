import web
import jsonrenderer
import dbhandler

urls = (
	"/topics", "AccessTopics",
	"/(.*)", "ModifyTopics",
	"/topics/load", "LoadTopics"
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
		return jsonrenderer.renderResponse( 
			"Update DB/storage here" )

application = web.application(urls, locals())
