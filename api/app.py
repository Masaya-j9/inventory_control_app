from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return {
    "app": "unko",
    "tutorial": "React, Flask and Docker"
  }

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)