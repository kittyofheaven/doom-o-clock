from flask import Flask
from flask_restful import Api, Resource, reqparse

from climate_predict import predict
from climate_data import get_climate_data
from doom_predict import doom_predict

app = Flask(__name__)
api = Api(app)

atmosphere_put_args = reqparse.RequestParser()
atmosphere_put_args.add_argument('Year', type=int, help='Insert Year to predict', required = True)
atmosphere_put_args.add_argument('Month', type=int, help='Insert Month to predict', required = True)
# the put req must be like this :
# {"Year" : 1993, "Month" : 11}

class Home(Resource):
    def get(self):
        return "api connected succesfully"

class Atmosphere(Resource):
    def get(self):
        get_data = doom_predict(450.00,310.00,310.00,300.00)
        return get_data
    
    def post(self):
        args = dict(atmosphere_put_args.parse_args())
        if args['Year'] > 2008:
            data = predict(args['Year'], args['Month']) 
        else :
            data = get_climate_data(args['Year'], args['Month'])
        return data, 200

api.add_resource(Home,"/")
api.add_resource(Atmosphere,"/atmosphere")

if __name__ == "__main__":
    app.run(debug=False)
