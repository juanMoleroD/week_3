from app import app

@app.route("/<name>")
def index(name):
    return f"<h1 style='font-size: 100px; color: red'>Hello {name}!</h1>"
    #return "<h1>Hello World!</h1>"

@app.route("/about")
def about():
    return "<h1>This is the new about page</h1>"