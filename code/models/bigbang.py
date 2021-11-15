from db import db


class BigBangLogModel(db.Model):
    __tablename__ = 'bigbanglog'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    result = db.Column(db.String(1000))

    def __init__(self, number, result):
        self.name = number
        self.result = result

    def json(self):
        return {'number': self.number, 'result': self.result}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
