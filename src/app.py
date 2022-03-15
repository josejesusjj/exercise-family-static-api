"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def  handle_get_all():
    members = jackson_family.get_all_members()
    data = request.json 
    last_name = jackson_family.last_name
    response_body = members
    return jsonify(response_body), 200

    #este es para capturar un solo miembro y falta terminar de definir


#o tambien:
@app.route('/members/<int:id>', methods=['GET'])
def handle_get(id):
    member = jackson_family.get_member(id)
    if member != None:
        return jsonify({'member': member}, 200, 'Ok')
    return jsonify({'message':'Not found'}, 404, 'error')

    
#@app.route('/members', methods=['POST'])
#def handle_add():
#    data = request.json
#    member = jackson_family.get_member(id)
#    if member == None:
#        return jsonify({'message':'Family member added'}), 200
        
#    else:
#        return jsonify({'message':'Missing data'}), 400
#    else: 
#        return jsonify({ "message": "Member already added" }, 400)  

    
# adding a member
@app.route('/members', methods=['POST'])
def handle_add():
    data = request.json
    members = jackson_family.add_member(data)
    return jsonify({'message':'Family member added'}), 200

    #deleting a member
#@app.route('/members/<int:id>', methods=['GET','DELETE'])
#def handle_delete():
#    member = jackson_family.delete_member(data)
#    jackson_family.delete_member(id) 
#    return jsonify({'message':'Family member removed'}), 200

@app.route('/members/<int:id>', methods=[ 'DELETE'])
def get_or_delete_member(id):
    member = jackson_family.get_member(id)

    if member == None:
        return jsonify({ "message": "Member not found" }, 404, 'Error')
    
    jackson_family.delete_member(id)    
    return jsonify({ "done": True }, 200, 'Ok')


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
