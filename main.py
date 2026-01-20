from flask import Flask

app = Flask(__name__)
app.run(debug=False)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/users")
def usuarios():
    return "<p>Bienvenido a usuarios</p>"

