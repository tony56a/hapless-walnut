import web
import jsonrenderer

def notFound():
	errorReason = "Resource not available"
	return web.notfound( jsonrenderer.renderError( errorReason ) )

def internalError():
	errorReason = "An exception has occured"
	return web.internalerror( jsonrenderer.renderError( errorReason ) )