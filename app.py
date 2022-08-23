"""
Example python app with the Flask framework: http://flask.pocoo.org/
"""
from os import environ

from flask import Flask, jsonify, redirect, url_for, request
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


# login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        if user == "TCG":
            return redirect(url_for('success', name=user))
        else:
            return redirect(url_for('failure', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('failure', name=user))


# login success
@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}'


# login failure
@app.route('/failure/<name>')
def failure(name):
    return f'Not right Company: {name}'


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
