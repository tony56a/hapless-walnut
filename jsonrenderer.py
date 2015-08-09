import json

RESULTGOOD = 'success'
RESULTFAILED= 'failed'
ERROR = 'error'
VALUE = 'value'

defaultResponse = { 'result': RESULTGOOD, VALUE:{} }
errorResponse = { 'result': RESULTFAILED, ERROR: 'Stuff.' }

def renderResponse( data ):
	returnValue = defaultResponse
	returnValue[ VALUE ] = data
	return json.dumps( returnValue )

def renderError( errorReason ):
	returnValue = errorResponse
	errorResponse[ ERROR ] = errorReason
	return json.dumps( returnValue )

