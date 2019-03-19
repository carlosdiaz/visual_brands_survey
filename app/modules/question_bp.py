from app import app
from flask import request, jsonify
from app.models.question_model import Question

__author__ = 'Carlos Diaz'
__version__ = '1.0'
__email__ = 'alberto.carlos@gmail.com'


@app.route('/get_questions/')
def get_question():
    get_all_questions = Question.query.all()

    for question in get_all_questions:
        print(question)

    return jsonify({'status': True})

