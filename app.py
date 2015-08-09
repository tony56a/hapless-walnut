import web
import json

urls = ("/.*", "hello")
app = web.application(urls, globals())

class hello:
    def GET(self):
        return json.dumps( 'Hello, world!' )

if __name__ == "__main__":
    app.run()