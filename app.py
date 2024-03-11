import random
import string

# Flask documentation and references can be found at: https://flask.palletsprojects.com/en/2.3.x/
from flask import Flask, url_for, request, render_template, make_response, abort, redirect, session, json, jsonify
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)
title = "Demonstration"

# Set the secret key to some random bytes. Keep this really secret!
decimal_num = random.random()
random_num = round(decimal_num * 10000000)
output_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
app.secret_key = str(random_num) + output_string


@app.route('/')
def index():
    return render_template('index.html', title=title)


@app.route('/redirect', methods=['GET', 'POST'])
def redirect():
    redirect_url = url_for('index')
    return redirect(redirect_url)


# Example of separating out Get and Post requests for /login, rather than writing: methods=['GET', 'POST']
@app.get('/login')
def login_get():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'


# Example of separating out Get and Post requests for /login, rather than writing: methods=['GET', 'POST']
@app.post('/login')
def login_post():
    return 'login'


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#             <form method="post">
#                 <p><input type=text name=username>
#                 <p><input type=submit value=Login>
#             </form>
#         '''
    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    # return render_template('login.html', error=error)


@app.route('/login_auth', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'login_auth'
    else:
        return 'login_auth'


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/hello-world')
def hello_world():
    return '<p>Hello, World</p>'


@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return f'{escape(username)}\'s profile'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {escape(post_id)}'


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')


@app.route('/upload-secure', methods=['GET', 'POST'])
def upload_file_secure():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")


@app.route('/path/<path:sub_path>')
def show_sub_path(sub_path):
    # show the sub_path after /path/
    return f'Sub_path {escape(sub_path)}'


# @app.route("/me")
# def me_api():
#     user = get_current_user()
#     return {
#         "username": user.username,
#         "theme": user.theme,
#         "image": url_for("user_image", filename=user.image),
#     }
#
# @app.route("/users")
# def users_api():
#     users = get_all_users()
#     return [user.to_json() for user in users]


@app.route('/post_form', methods=['POST'])
def process_form():
    if request.method == 'POST':
        data = request.form
        print(data['username'])
        print(data['password'])
        return data
    elif request.method == 'GET':
        return render_template('form.html')
    else:
        return "Method not allowed. Please use POST or GET."


@app.route('/projects/', methods=['GET', 'POST'])
def projects():
    my_projects = {
        "project1": {
            "name": "project1",
            "date": "2024-01-01"
        },
        "project2": {
            "name": "project2",
            "date": "2024-01-01"
        }
    }
    if request.method == 'GET':
        return jsonify(my_projects)
    elif request.method == 'POST':
        # To call and test this POST:
        # curl -XPOST --location '127.0.0.1:5000/projects' --header 'Content-Type: application/json' --data '{"data":"one"}'
        # Get request:
        # curl --location --request GET '127.0.0.1:5000/projects' --header 'Content-Type: application/json'
        params = request.get_json()  # > {"data":"one"}
        params_keys = params.keys()
        param_key = [i for i in params_keys][0]
        params_values = params.values()
        param_value = [i for i in params_values][0]
        my_projects[f"project{param_key}"] = dict()
        my_projects[f"project{param_key}"]["name"] = param_key
        my_projects[f"project{param_key}"]["parameter_value"] = param_value
        my_projects[f"project{param_key}"]["date"] = "2024-01-01"
        # app.logger.debug(my_projects)
        return my_projects
    else:
        redirect(url_for('page_not_found'))
    return 'The project page'


@app.route('/api', methods=['GET'])
def api():
    api_dict = {
        "apis": {
            '/': {
                'type': 'string',
                'methods': [
                    'get'
                ],
                'returns': 'html'
            },
            'login': {
                'type': 'session',
                'methods': [
                    'get',
                    'post'
                ],
                'returns': 'session'
            },
            'login_auth': {
                'type': 'json',
                'methods': [
                    'get'
                ],
                'returns': 'html code'
            },
            'logout': {
                'type': 'session',
                'methods': [
                    'get'
                ],
                'returns': 'session'
            },
            'hello': {
                'type': 'string',
                'methods': [
                    'get'
                ],
                'returns': 'string'
            },
            'hello/<name>': {
                'type': 'string',
                'methods': [
                    'get'
                ],
                'returns': 'string'
            },
            'hello-world': {
                'type': 'string',
                'methods': [
                    'get'
                ],
                'returns': 'string'
            },
            'user/<username>': {
                'type': 'string',
                'methods': [
                    'get'
                ],
                'returns': 'string'
            },
            'post/<post_id>': {
                'type': 'int',
                'methods': [
                    'get'
                ],
                'returns': 'int'
            },
            'upload': {
                'type': 'file',
                'methods': [
                    'post'
                ],
                'returns': 'none'
            },
            'upload-secure': {
                'type': 'file',
                'methods': [
                    'post'
                ],
                'returns': 'none'
            },
            'path/<sub_path>': {
                'type': 'path',
                'methods': [
                    'get'
                ],
                'returns': 'string'
            },
            'post_form': {
                'type': 'file',
                'methods': [
                    'post'
                ],
                'returns': 'html'
            },
            'projects': {
                'type': 'json',
                'methods': [
                    'get',
                    'post'
                ],
                'returns': 'json'
            },
            'about': {
                'type': 'string',
                'methods': [
                    'get'
                ],
                'returns': 'string'
            }
        }
    }
    return api_dict


@app.route('/about')
def about():
    return 'The about page'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

app.logger.debug('Debug: Debugging - Test')
app.logger.warning('Warning: Warning - Test (%d exceptions caught)', 10)
app.logger.error('Error: Error - Test')
