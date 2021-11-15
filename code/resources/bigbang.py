import json

from flask_restful import Resource, reqparse
from business.bigbang import BigBangLogic
from models.bigbang import BigBangLogModel


class BigBang(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('number',
                        type=int,
                        required=True,
                        help="number cannot be blank!"
                        )

    def post(self):
        data = BigBang.parser.parse_args()
        number = data['number']
        result = BigBangLogic(int(number)).calculate_string_based_on_number()
        try:
            bigbang_model = BigBangLogModel(int(number), str(result))
            bigbang_model.save_to_db()
        except:
            return {"message": "Error inserting data!"}, 500
        return result, 201

