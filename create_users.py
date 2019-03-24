from app import db
from app.models.user import User
from werkzeug.security import generate_password_hash

__author__ = 'Carlos Diaz'
__version__ = '1.0'
__email__ = 'alberto.carlos@gmail.com'


class MigrateUsers:

    @staticmethod
    def migrate_users():

        user_list = {('1', 'carlos@gmail.com', '123', 1),
                     ('2', 'isra@gmail.com', '456', 2)}

        for user in user_list:
            print(user[0], user[1])
            db.session.add(User(user[0], user[1],
                                generate_password_hash(user[2]), user[3]))

        db.session.commit()

MigrateUsers.migrate_users()



