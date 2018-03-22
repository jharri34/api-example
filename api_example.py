from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask_jsonpify import jsonify
import os
import subprocess

# db_connect = create_engine('sqlite:///members.db')
app = Flask(__name__)
api = Api(app)

#example ignore
# class members(Resource):
#     def get(self):
#         conn = db_connect.connect()
#         query = conn.execute("select * from members")
#         result = {'members': [i for i in query.cursor.fetchall()]}
#         return jsonify(result)
# #example ignore
# class member(Resource):
#     def get(self, member):
#         conn = db_connect.connect()
#         query = conn.execute("select * from members where id =%d "  %int(member))
#         result = {'data': query.cursor.fetchall()}
#         return jsonify(result)

class bash_command(Resource):
    def get (self, cmd):
        #example bash_command('a="Apples and oranges" && echo "${a/oranges/grapes}"')
        #https://stackoverflow.com/questions/32730729/is-it-possible-to-create-a-fully-self-contained-python-package
        subprocess.Popen(cmd, shell=True, executable='/bin/bash')

class root(Resource):
    def get(self):
        return "Hello from Jay!"


api.add_resource(member,'/member/<member>')
api.add_resource(members, '/members')
api.add_resource(root,'/')
api.add_resource(bash_command,'/bash/<cmd>')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
