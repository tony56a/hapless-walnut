"""
Main web application
"""

import web
import jsonrenderer
import errorhandlers
import birdie

urls = (
	"/", "Index",
	# Use a sub-app to handle Birdie REST calls
	'/birdie/rest', birdie.application
)

# Just testing
class Index:
    def GET(self):
        return jsonrenderer.renderResponse( 'Hello, world!' )

app = web.application(urls, globals())
# Route all uncaught errors to produce a JSON response instead
app.notfound = errorhandlers.notFound
app.internalerror = errorhandlers.internalError

if __name__ == "__main__":
	app.run()