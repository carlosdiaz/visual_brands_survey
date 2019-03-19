from flask import Flask
from flask import jsonify
from app import app

from app import manager
from app.models.question_model import Question


# start the development server using the run() method
if __name__ == "__main__":
    #manager.run()
    app.run(debug=True, port=5000)