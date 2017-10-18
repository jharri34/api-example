from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask_jsonpify import jsonify
import os

db_connect = create_engine('sqlite:///members.db')
app = Flask(__name__)
api = Api(app)


class members(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from members")
        result = {'members': [i for i in query.cursor.fetchall()]}
        return jsonify(result)

class member(Resource):
    def get(self, member):
        conn = db_connect.connect()
        query = conn.execute("select * from members where id =%d "  %int(member))
        result = {'data': query.cursor.fetchall()}
        return jsonify(result)

@app.route("/")
def hello():
    return "Hello from Python!"

api.add_resource(member,'/member/<member>')
api.add_resource(members, '/members') # Route_1



if __name__ == '__main__':
     port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
