import web
import json

with open('app.conf') as configFile:    
    config = json.load(configFile)