from flask import Flask, jsonify
from flask_migrate import Migrate, Manager, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

def create_app():
    # create the application object
    app = Flask(__name__)
    app.config.from_pyfile('/home/carlos/PycharmProjects/visual_brands_survey/app_config.py')
    return app

app = create_app()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@app.route("/")
def hello_world():
    result = db.engine.execute("select * from smart_message.mobile_mt;")
    names = [row[0] for row in result]
    print(names)
    return "Hello, World!"


@app.route('/get_questions/')
def get_question():
    from app.models.question_model import Question
    response_list = list()

    get_all_questions = Question.query.all()

    for question in get_all_questions:
        print(question)
        response_list.append(question.question_name)

    return jsonify({'responses': response_list})

