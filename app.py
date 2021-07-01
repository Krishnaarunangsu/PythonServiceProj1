"""
Example python app with the Flask framework: http://flask.pocoo.org/
"""
import json
from os import environ

from flask import Flask, jsonify, request, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    """

    :return:
    """
    return render_template('index.html', powered_by=environ.get('POWERED_BY', 'Deis'))


# https://riptutorial.com/flask/example/5831/return-a-json-response-from-flask-api
@app.route('/api/get-json')
def hello():
    return jsonify(hello='world')  # Returns HTTP Response with {"hello": "world"}


# https://techtutorialsx.com/2017/01/07/flask-parsing-json-data/
# https://github.com/deis
# https://github.com/IBM/python-flask-app/blob/master/Dockerfile
# https://github.com/digitalocean/sample-flask
# https://github.com/codefresh-contrib/python-flask-sample-app
# https://github.com/bradtraversy/myflaskapp
# https://github.com/bigcommerce/hello-world-app-python-flask
# https://github.com/XD-DENG/flask-example/blob/master/app.py
# https://realpython.com/flask-by-example-part-1-project-setup/
# https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
# https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask
# https://pythonhosted.org/Flask-JSON/
# https://pythonbasics.org/flask-rest-api/
# https://www.kite.com/python/answers/how-to-return-a-json-response-using-flask-in-python
# https://www.freecodecamp.org/news/build-a-simple-json-api-in-python/
# https://pythonise.com/series/learning-flask/working-with-json-in-flask
# https://www.geeksforgeeks.org/how-to-return-a-json-object-from-a-python-function/

@app.route('/api/get-person')
def get_person():
    person = {'name': 'Alice', 'birth-year': 1986}
    return jsonify(person)


@app.route('/api/get-people')
def get_people():
    people = [{'name': 'Alice', 'birth-year': 1986},
              {'name': 'Bob', 'birth-year': 1985}]
    return jsonify(people)


@app.route('/')
def api_root():
    return 'Welcome'


@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')


@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid


@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'


@app.route('/echo', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PATCH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"


@app.route('/messages', methods=['POST'])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"
    else:
        return "415 Unsupported Media Type ;)"


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run()
