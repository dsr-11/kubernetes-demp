from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """Function to test the functionality of the API"""
    return "Hello, buddy!! its RAHUL"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
