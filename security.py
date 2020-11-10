from werkzeug.security import safe_str_cmp # used to safely compare strings.
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password): # comparing strings with == not advised with different versions of python etc.
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)


print("---Security module complete---")

