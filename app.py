from flask import Flask, url_for, request, render_template, make_response, abort, redirect, session
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    username = request.cookies.get('username')
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
    # return 'Index Page'
    # if 'username' in session:
    #     return f'Logged in as {session["username"]}'
    # return 'You are not logged in'


@app.route('/login_auth', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'login_auth'
    else:
        return 'login_auth'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
            <form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''
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

# @app.get('/login')
# def login_get():
#     return 'login'
# @app.post('/login')
# def login_post():
#     return 'login'


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/hello-world')
def hello():
    return '<p>Hello, World</p>'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return f'{username}\'s profile'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


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


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


# @app.route("/users")
# def users_api():
#     users = get_all_users()
#     return [user.to_json() for user in users]


# @app.route("/me")
# def me_api():
#     user = get_current_user()
#     return {
#         "username": user.username,
#         "theme": user.theme,
#         "image": url_for("user_image", filename=user.image),
#     }


@app.route('/projects/')
def projects():
    return 'The project page'


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

app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')
