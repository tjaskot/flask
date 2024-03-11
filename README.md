# Flask Micro Api App

basic flask app with routes and endpoints for testing local servers and services in micro api framework

Run program commands:

Development Server
- flask --app app run --debug

Production Server
- waitress-serve --host 127.0.0.1 app:app

Api Listing
- /
- login
- login_auth
- logout
- hello
- hello/<name>
- hello-world
- user/<username>
- post/<post_id>
- upload
- upload-secure
- path/<sub_path>
- post_form
- projects
- about
