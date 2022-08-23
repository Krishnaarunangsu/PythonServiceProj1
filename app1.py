"""
Example python app with the Flask framework: http://flask.pocoo.org/
"""
import json
from os import environ

from flask import Flask, jsonify, request, url_for
from flask import render_template

app = Flask(__name__)


# Welcome Page default method is GET
@app.route('/')
def index():
    """
    index.html page
    :return:
    """
    return render_template('index.html', powered_by=environ.get('POWERED_BY', 'TCG'))


# Returns response in JSON Format
@app.route('/api/get-json')
def hello():
    """

    :return: JSON Response
    """
    return jsonify(hello='world')  # Returns HTTP Response with {"hello": "world"}


# Get a Particular Person
@app.route('/api/get-person')
def get_person():
    """

    :return:
    """
    person = {'name': 'Alice', 'birth-year': 1986}
    return jsonify(person)


# Get the people
@app.route('/api/get-people', methods=['GET'])
def get_people():
    """

    :return:
    """

    people = [{'name': 'Alice', 'birth-year': 1986},
              {'name': 'Bob', 'birth-year': 1985}]

    for key, value in people.iteritems():
        print(f'{key}')
    return jsonify(people)


# Get the people
@app.route('/api/get-people/<name>', methods=['GET'])
def get_people_year():
    """

    :return:
    """
    people = [{'name': 'Alice', 'birth-year': 1986},
              {'name': 'Bob', 'birth-year': 1985}]
    return jsonify(people)


@app.route('/')
def api_root():
    """
    Default Method is GET
    :return:
    """
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


@app.route('/hello_res', methods=['GET'])
def get_api_hello_resp():
    """

    :return:
    """
    data = {
        'hello': 'world',
        'number': 3
    }
    resp_json = json.dumps(data)
    # response = Response(resp_json, status=200, mimetype='application/json')

    response = jsonify(resp_json)
    response.status_code = 200
    response.headers['Link'] = 'http://luisrei.com'

    return response


@app.errorhandler(404)
def user_id_not_found(error=None):
    error_message = {
        'status': 404,
        'message': 'User Id not found:' + request.url
    }
    response = jsonify(error_message)
    response.status_code = 404
    return response


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_details(user_id):
    """

    :param user_id:
    :return: user if id exists else error message
    """
    users = {1: 'Ram', '2': 'Krishna', '3': 'Jagannath'}
    if user_id in users:
        # return users[user_id]
        return jsonify({user_id: users[user_id]})
    else:
        return user_id_not_found()


@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    """

    :param uuid:
    :return:
    """
    content = request.json
    print(f'Content is:{content["mytext"]}')
    return jsonify({"uuid": uuid,
                    "text_value": content["mytext"]})


@app.route('/api/add_message7', methods=['POST'])
def add_message7():
    """

    :param uuid:
    :return:
    """
    content = request.json
    print(f'Content is:{content["mytext"]}')
    return jsonify({"text_value": content["mytext"],
                    "status": "SUCCESS"})


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run()
