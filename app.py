"""
Example python app with the Flask framework: http://flask.pocoo.org/
"""

from os import environ

from flask import Flask, jsonify, url_for
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


@app.route('/articles')
def get_api_articles():
    return "List of " + url_for('get_api_articles')


@app.route('/articles/<article_id>')
def get_api_article(article_id):
    try:
        if isinstance(int(article_id), int):
            print('hu')
            return "You are reading article " + article_id
    # return "You are reading article " + str(article_id) ERROR-500 Internal server error
    except ValueError:
        return "Article id is not integer"


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run()
