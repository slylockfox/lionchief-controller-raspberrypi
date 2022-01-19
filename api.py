from urllib import request
from flask import Flask, request
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

@app.route('/forward',methods=['GET', 'POST'])
def forward():
    if request.method == 'POST':
        lion.go()
    if request.method == 'GET':
        speed = request.args.get('speed',default=0,type=int)
        lion.go(speed)
    return {'moving':'now'}


@app.route('/currentSpeed',methods=['GET'])
def currentSpeed():
    return {'Current Speed':lion._speed}

@app.route('/direction', methods=['GET'])
def reverse():
    requstDirection =request.args.get('reverse',default=False, type= lambda v: v.lower()=='true')
    print(requstDirection)
    if requstDirection==False:
        lion.forward()
    else:
        lion.reverse()    
    return {'Current Direction': 'reverse' if lion._reverse==True else 'forward'}

if __name__ == '__main__':
    #serve(app,host='0.0.0.0',port=5000)
    app.run(host='0.0.0.0',port=8080)