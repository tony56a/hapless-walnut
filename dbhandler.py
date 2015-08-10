import web
from sqlite3 import IntegrityError,OperationalError

db = web.database(dbn='sqlite', db='topics.db')

def addEntry( topic, url=None ):
	try:
		db.insert( 'topics', name=topic, url=url )
		return None
	except IntegrityError:
		# Or, attempt update on row maybe?
		return "Topic already exists"
	except OperationalError as e:
		web.debug( e )
		return "Error during operation"

def queryEntries( topic, showURLs=False ):
	try:
		returnValue = []
		queryResult = None

		if topic:
			params = dict(name=topic+'%')
			queryResult = db.select('topics', params, where="name LIKE $name", limit=50)
		else:
			queryResult = db.select( "topics", limit=50)

		if returnValue:
			for value in queryResult:
				returnValue.append( dict( value ) )
		else:
			for value in queryResult:
				returnValue.append( value.name )

		return returnValue
	except OperationalError as e:
		web.debug( e )
		return "Error during operation"

def removeEntry( topic ):
	try:
		db.delete( 'topics', where='name=$topic', vars=locals() )
		return None
	except IntegrityError:
		return "Not possible to remove"
	except OperationalError as e:
		web.debug( e )
		return "Error during operation"
	
