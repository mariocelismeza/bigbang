import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from code.models.bigbang import BigBangLogModel
from db import db


class TestStudentModel(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.session = Session(self.engine)
        db.metadata.create_all(self.engine)
        self.mock_result = str([
                        "1",
                        "2",
                        "Big",
                        "4",
                        "Bang",
                        "Big",
                        "Theory",
                        "8",
                        "Big",
                        "Bang",
                        "11",
                        "Big",
                        "13",
                        "Theory",
                        "BigBang",
                        "16",
                        "17",
                        "Big",
                        "19",
                        "Bang",
                        "BigTheory"
                    ])
        self.result = BigBangLogModel(21, result=self.mock_result)
        self.session.add(self.result)
        self.session.commit()

    def test_save_student(self):
        expected = [self.result]
        result = self.session.query(BigBangLogModel).all()
        self.assertEqual(expected, result)

    def tearDown(self):
        db.metadata.drop_all(self.engine)