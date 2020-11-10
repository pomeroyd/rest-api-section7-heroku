from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource): #Student class is a copy of Resource class
    parser = reqparse.RequestParser() # parser belongs to class itself.
    parser.add_argument('price', 
        type=float,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('store_id', 
        type=int,
        required=True,
        help="Every item needs a store id."
    )
    
    #not need to do decorator @app.route etc
    @jwt_required() #security decorator
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        
        
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            #item matches the name
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
            #this is a bad request. client should have known. return a bad request status.
        data = Item.parser.parse_args()
        
        item = ItemModel(name, data['price'], data['store_id'])  # object with name and price. Can also give it **data
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"},500 #internal server error

        return item.json(), 201 # add status code for "created" # returning a json.

    #@jwt_required() #security decorator add this if you want to add security to a feature
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}
        

    #use reqparse
    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        
        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']

        item.save_to_db()
            
        return item.json()

    

#Now we have two working endpoints.
#Things to improve.
#what to do if item is not found? Currently null is returned. This is not JSON.
#Done
#Post return status code 201. DONE

#Add resource for Item list

class ItemList(Resource):
    def get(self):
        #list comprehension.
        return {'items': [item.json() for item in ItemModel.query.all()]}
        #way using lambda
        #return {'items': list(map(lambda z: x:json(), ItemModel.query.all()))}
