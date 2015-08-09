import web
import jsonrenderer

urls = (
	"/topics", "AccessTopics",
	"/topics/load", "LoadTopics"
)

class AccessTopics:
	def GET( self ):
		return jsonrenderer.renderResponse( [
			web.input(),[ 'a','b','c','d']] )

	def POST( self ):
		return jsonrenderer.renderResponse( web.input() )


	def DELETE( self ):
		return jsonrenderer.renderResponse( "Deleted: " )

class LoadTopics:
	def GET( self ):
		return jsonrenderer.renderResponse( 
			"Update DB/storage here" )

application = web.application(urls, locals())
