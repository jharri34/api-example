from flask import Flask, request

app = Flask(__name__)
api = Api(app)


class member(Resource):
    def get(self):
        return 'Joe, John, Carl'

api.add_resource(member, '/member') # Route_1



if __name__ == '__main__':
     app.run(port='5002')
