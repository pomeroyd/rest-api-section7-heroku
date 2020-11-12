#Make sure conda environment is setup correctly
# conda info
#conda env list
#https://towardsdatascience.com/manage-your-python-virtual-environment-with-conda-a0d2934d5195

import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT # decorator


from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

print("---All Modules Loaded---")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db') #can be any type of databse type, mysql, sqlite, oracle
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose' # if this was a production code, this key should not be publicly accessible.
api = Api(app)



jwt = JWT(app, authenticate, identity) #new endpoint /auth. sends it username and password.
# creates a jw token if user identified correctly





#add correct endpoints
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/item/name
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')





#only run app if the program is __main__ and not a file that is being imported.
if __name__ == '__main__':
    app.run(port=5000, debug=True) # add html debug page
