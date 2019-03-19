from app import db

__author__ = 'Carlos Diaz'
__version__ = '1.0'
__email__ = 'alberto.carlos@gmail.com'

question_answer = db.Table(
    'question_answer', db.Model.metadata,
    db.Column('question_id', db.Integer(), db.ForeignKey('question.id')),
    db.Column('answer_id', db.Integer(), db.ForeignKey('answer.id')),
)


class Answer(db.Model):

    __tablename__ = 'answer'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    answer_name = db.Column(db.String(200), index=True, unique=False)
    answer_type = db.Column(db.String(100), index=True, unique=False)

    def __init__(self, answer_name, answer_type):
        self.answer_name = answer_name
        self.answer_type = answer_type

    def __repr__(self):
        return '<Answer %s %s>' % (self.answer_name, self.answer_type)

