from flask import Flask, Request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

from flask import jsonify, request
from climate_predict import predict
from climate_data import get_climate_data
from doom_predict import doom_predict

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/": {"origins": "*"}})


atmosphere_put_args = reqparse.RequestParser()
atmosphere_put_args.add_argument('Year', type=int, help='Insert Year to predict')
atmosphere_put_args.add_argument('Month', type=int, help='Insert Month to predict')
# the put req must be like this :
# {"Year" : 1993, "Month" : 11}

class Home(Resource):
    def get(self):
        return "api connected succesfully"

class Atmosphere(Resource):
    def get(self):
        get_data = doom_predict(450.00,310.00,310.00,300.00)
        response = jsonify(get_data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
    def post(self):
        print(request.data)
        args = dict(atmosphere_put_args.parse_args())
        print(args)
        if args['Year'] > 2008:
            data = predict(args['Year'], args['Month']) 
            response = jsonify(data)
            response.headers.add('Access-Control-Allow-Origin', '*')
        else :
            data = get_climate_data(args['Year'], args['Month'])
            response = jsonify(data)
            response.headers.add('Access-Control-Allow-Origin', '*')
        # print(response)
        return response

    def options(self):
        print(request.data)
        args = dict(atmosphere_put_args.parse_args())
        print(args)
        if args['Year'] > 2008:
            data = predict(args['Year'], args['Month']) 
            response = jsonify(data)
            response.headers.add('Access-Control-Allow-Origin', '*')
        else :
            data = get_climate_data(args['Year'], args['Month'])
            response = jsonify(data)
            response.headers.add('Access-Control-Allow-Origin', '*')
        # print(response)
        return response

# class Atmosphere2(Resource):
#     def get(self, Year, Month):
#         get_data = doom_predict(450.00,310.00,310.00,300.00)
#         response = jsonify(get_data)
#         response.headers.add('Access-Control-Allow-Origin', '*')
#         return response

api.add_resource(Home,"/")
api.add_resource(Atmosphere,"/atmosphere")
# api.add_resource(Atmosphere2,"/atmosphere2/<int:Year>/<int:Month>")

if __name__ == "__main__":
    app.run(debug=False)
