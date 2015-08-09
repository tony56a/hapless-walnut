import json

RESULTGOOD = 'Success'
RESULTFAILED= 'Failed'
ERROR = 'Error'
VALUE = 'Value'

defaultResponse = { 'Result': RESULTGOOD, VALUE:{} }
errorResponse = { 'Result': RESULTFAILED, ERROR: 'Stuff.' }

def renderResponse( data ):
	returnValue = defaultResponse
	returnValue[ VALUE ] = data
	return json.dumps( returnValue )

def renderError( errorReason ):
	returnValue = errorResponse
	errorResponse[ ERROR ] = errorReason
	return json.dumps( returnValue )

