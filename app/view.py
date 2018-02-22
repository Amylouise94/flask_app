"""Main module."""
from flask import render_template
from app import app
import sysinfo

@app.route('/')
def index():
        returnDict = {}
        returnDict['user'] = 'Amy'
        returnDict['title'] = 'Flask Application'
	returnDict['info'] = sysinfo.main()
        return render_template("index.html", **returnDict)

