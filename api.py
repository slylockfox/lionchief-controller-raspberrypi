from flask import Flask
from flask_restful import Resource, Api
from waitress import serve
from webapi import LionApi

app = Flask(__name__)
app.debug=True

api = Api(app)

lion = LionApi()

class HelloWorld(Resource):
    def get(self):
        return {'hello':'World2'}
    
api.add_resource(HelloWorld, '/2')

@app.route('/',methods=['GET'])
def something():
    lion.start()
    return 'BoB'

@app.route('/horn', methods=['GET'])
def horn():
    lion.horn()
    return {'horn':'on'}

if __name__ == '__main__':
    #serve(app,host='0.0.0.0',port=5000)
    app.run(host='0.0.0.0',port=8080)