#instead of dictionary, use proper objects
import sqlite3 # add ability to interact with database
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        #check if new username already exists
        if UserModel.find_by_username(data['username']):
            return {"message" : "A user with that username already exists"},400

        user = UserModel(**data) # for each key unpack the dictionary
        user.save_to_db()

        return {"message" : "User created Successfully."}, 201

    


print("---User module complete---")