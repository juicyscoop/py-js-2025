from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello user!"

@app.route("/hello/<int:name>")
def hello_name(name):
    print(f"Received int: {name}")
    converted = int(name)
    print(f"Converted: {converted}")
    return str(name)

if __name__=="__main__":
    app.run(debug=True)

