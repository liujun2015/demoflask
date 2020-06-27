from flask import render_template

from demoflask.app import app
from demoflask.models import TestMethod


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/automation/testMethod')
def getTestMethod():
    testMethods = TestMethod.query.all()
    return render_template('testMethod.html', methodList=testMethods)

