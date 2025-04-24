from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask App"

@app.route('/about')
def about():
    return "Hi my name is Ben, This is my Flask project for IT112."

if __name__ == '__main__':
    app.run(debug=True)