"""
Methods to interface with the database
"""

import web
import conf
from sqlite3 import IntegrityError,OperationalError


#database object, ensure that sqlite3 database has been created prior to starting server 
db = web.database(dbn='sqlite', db=conf.config['dbfile'])

def addEntry( topic, url=None ):
	"""
	Add an entry to the DB
	"""
	try:
		db.insert( 'topics', name=topic, url=url )
		return None
	except IntegrityError:
		# Return error to user, or, attempt update on row maybe?
		return "Topic already exists"
	except OperationalError as e:
		web.debug( e )
		return "Error during operation"

def queryEntries( topic, page, showURLs=False ):
	"""
	Query db for topics
	"""
	try:
		returnValue = []
		queryResult = None
		page = page * 10
		if topic:
			# if topic query string is available, add it to query
			params = dict(name=topic+'%')
			# only fetch 10 topics at a time
			queryResult = db.select('topics', params, where="name LIKE $name", 
				limit= str( page ) + ',10' )
		else:
			queryResult = db.select( "topics", limit= str( page ) + ',10' )

		# if not showing urls, just return the name instead of the whole dict
		if showURLs:
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
	"""
	Remove an entry from the DB
	"""
	try:
		db.delete( 'topics', where='name=$topic', vars=locals() )
		return None
	except IntegrityError:
		# In case remove violates db constraints, report issue to user
		return "Not possible to remove"
	except OperationalError as e:
		web.debug( e )
		return "Error during operation"
	
