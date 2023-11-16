# import json
import json

# import flask, jsonify, request
from flask import Flask, jsonify, request

# import custom functions from helper
from Helper import get_users, create_user, get_user, update_user, delete_user

# create an instance of Flask
app = Flask(__name__)

# define port number
port = 3000


# get all users
@app.route('/api/users', methods=['GET'])
def getUsers():
    
    # get all users from get users function
    users = get_users()

    # return the users array
    return jsonify(users)

# get user by id
@app.route('/api/users/<int:id>', methods=['GET'])
def getUser(id):

    # get user from get user function by passing id as the argument
    # store it in user variable
    user = get_user(id)

    # use condition to check the value of user variable 
    if user is None:
        # if the user is none, throw an error
        return jsonify({'error': 'User does not exist'}), 404
    
    # if the user is not none, return the user object
    return jsonify(user), 200

# create user 
@app.route('/api/users', methods=['POST'])
def createUser():
    # load the user request body/data and store it
    # in user variable
    user = json.loads(request.data)
    
    # call the create user function
    # pass user as an argument
    # store the result in a variable call create_user
    created_user = create_user(user)

    # return the newly created user object with an id
    return jsonify(created_user), 201

# updated user by id
@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user_by_id(id):
    # load the user request body/data and store it
    # in an updated_user_data variable
    updated_user_data = json.loads(request.data)

    # call the update user function
    # pass updated user data and id as an argument
    # store the result in a variable call create_user
    user = update_user(updated_user_data, id)

     # use condition to check the value of user variable 
    if user is None:
        # if the user is none, throw an error
        return jsonify({'error', 'User does not exist'}), 404
    
    # if the user is not none, return the user object
    return jsonify(user), 200

# delete user
@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    # call delete user function
    user = delete_user(id)

    # use condition to check the value of user variable 
    if user is None:
        # if the user is none, throw an error
        return jsonify({'error': 'User does not exist'}), 404

    # if the user is not none, return the user object
    return jsonify(user), 200

# run the app on the specified port
# pass the port number as an argument
app.run(port=port)
