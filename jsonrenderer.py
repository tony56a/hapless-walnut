"""
Methods to render JSON output for error and method reponses
"""

import json
import conf

RESULTGOOD = 'success'
RESULTFAILED= 'failed'
ERROR = 'error'
VALUE = 'value'

def renderResponse( data ):
	"""
	For standard responses
	"""
	defaultResponse = { 'version': conf.config['version'], 'result': RESULTGOOD, VALUE:{} }
	returnValue = defaultResponse
	returnValue[ VALUE ] = data
	return json.dumps( returnValue )

def renderError( errorReason ):
	"""
	For notifying the user of errors
	"""
	errorResponse = { 'version': conf.config['version'], 'result': RESULTFAILED, ERROR: 'Stuff.' }
	returnValue = errorResponse
	errorResponse[ ERROR ] = errorReason
	return json.dumps( returnValue )

