from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Product(Resource):
	def get(self):
		return {
			'products': ['Babi','Coklat','Buah','Ayam Goreng']
		}

class Test(Resource):
	def get(self):
		return {
			'products': ['Sapi','Ramen','Tempe','Kuah']
		}

class Default(Resource):
    def get(self):
        return {
            "result": ["Connection to API Server Established"]
        }

api.add_resource(Product,'/product')
api.add_resource(Test,'/test')
api.add_resource(Default,'/')
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
