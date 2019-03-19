from app import db
from app.models.answer_model import question_answer

__author__ = 'Carlos Diaz'
__version__ = '1.0'
__email__ = 'alberto.carlos@gmail.com'


class Question(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    question_name = db.Column(db.String(200), index=True, unique=False)
    question_type = db.Column(db.String(100), index=True, unique=False, default='simple')
    answers = db.relationship('Answer', secondary=question_answer, backref=db.backref('answer', lazy='dynamic'))

    def __init__(self, question_name, question_type):
        self.question_name = question_name
        self.question_type = question_type

    def __repr__(self):
        return '<Question %s %s>' % (self.question_name, self.question_type)
