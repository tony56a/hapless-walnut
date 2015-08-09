import web
import jsonrenderer
import errorhandlers
import birdie
import conf

urls = (
	"/", "Index",
	'/birdie/rest', birdie.application
)

class Index:
    def GET(self):
        return jsonrenderer.renderResponse( 'Hello, world!' )

app = web.application(urls, globals())
app.notfound = errorhandlers.notFound
app.internalerror = errorhandlers.internalError

if __name__ == "__main__":
    app.run()