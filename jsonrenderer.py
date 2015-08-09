import json
import conf

RESULTGOOD = 'success'
RESULTFAILED= 'failed'
ERROR = 'error'
VALUE = 'value'

defaultResponse = { 'version': conf.config['version'], 'result': RESULTGOOD, VALUE:{} }
errorResponse = { 'version': conf.config['version'], 'result': RESULTFAILED, ERROR: 'Stuff.' }

def renderResponse( data ):
	returnValue = defaultResponse
	returnValue[ VALUE ] = data
	return json.dumps( returnValue )

def renderError( errorReason ):
	returnValue = errorResponse
	errorResponse[ ERROR ] = errorReason
	return json.dumps( returnValue )

