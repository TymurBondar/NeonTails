from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})



@app.route('/')
def index():
    return {"message": "Welcome to NeonTails!"}

@app.route('/api/message', methods=['GET'])
def view_message():
    return {"message": "NOBODY BUILDS FLASK APPLICATIONS BETTER THAN ME!"}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)