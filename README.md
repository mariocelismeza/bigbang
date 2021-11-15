# bigbang

Steps to start the app

1. Execute the followings commands in the root of the project
#virtualenv venv --python=python3.8
    #source venv/bin/activate
    --Installing libs I need
    #pip install Flask
    #pip install Flask-RESTful
    #pip install Flask-SQLAlchemy

    --Execute
    #python code/app.py

endpoint: 
http://127.0.0.1:5000/bigbang

Verb: POST

Body:
{
	"number": 21
}