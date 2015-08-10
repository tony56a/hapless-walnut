"""
Config loader, just loads API keys, version numbers, etc
in a JSON file as a dictionary
"""
import web
import json

with open('app.conf') as configFile:
	config = json.load(configFile)