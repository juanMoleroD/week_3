from flask import Flask

app = Flask(__name__)
#controllers after the app
from controllers import controller 

#in the terminal you need to type export FLASK_APP=app.py
#run on terminal using flask run , which is the same as python3 -m flask run
#or you could add the .flaskenv after installing the python-dotenv 

if __name__ == '__main__':
    app.run(debug = True)
