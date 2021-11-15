from flask_restful import Resource, reqparse

from models.student import StudentModel


class Student(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phone',
                        type=str,
                        required=True,
                        help="Evey item needs a store id."
                        )
    parser.add_argument('code',
                        type=str,
                        required=True,
                        help="Evey item needs a store id."
                        )

    def get(self, name):
        pass

    def post(self, name):
        data = Student.parser.parse_args()
        student = StudentModel(name, **data)
        try:
            student.save_to_db()
        except Exception as e:
            print(e)
            return {"message": "Error inserting data!"}, 500
        return student.json(), 201


class StudentList(Resource):
    def get(self):
        pass