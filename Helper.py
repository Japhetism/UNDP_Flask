# default user list
users = [
    {
        "id": 1,
        "first_name": "James",
        "last_name": "Doe",
        "email": "jamesdoe@gmail.com",
        "username": "Jdoe"
    },
    {
        "id": 2,
        "first_name": "Jone",
        "last_name": "David",
        "email": "jonedavid@gmail.com",
        "username": "Jdavid"
    },
    {
        "id": 3,
        "first_name": "Ken",
        "last_name": "Ben",
        "email": "kenben@gmail.com",
        "username": "KBen"
    }
]

# function to get all users
def get_users():
    # return all users
    return users

# function to create user
def create_user(user):
    # get the last user id
    # increment the last user id by 1
    user['id'] = get_last_user_id() + 1

    # store the new user in users list
    users.append(user)

    # return the new user with the new id assigned
    return user

# function to get user
def get_user(id):
    # function to get a user by iterating through the users list
    user = get_user_by_id(id)
    
    # return user
    return user

# function to update user
def update_user(user_updated_data, id):
    # function to get a user by iterating through the users list
    user = get_user_by_id(id)

    # test for condition to determine if the user is not NONE
    if user is None:
        # return None if the user is None
        return None
    
    # update the user in the users list
    user.update(user_updated_data)

    # return the updated users
    return user

# function to delete user
def delete_user(id):
    # function to get a user by iterating through the users list
    user = get_user_by_id(id)

    # test for condition to determine if the user is not NONE
    if user is None:
        # return None if the user is None
        return None
    
    # iterate through the users list and 
    # return all users that does not match the id
    updated_users = [u for u in users if u['id'] != id]

    # clear your users array of user objects
    users.clear()

    # iterate through the newly updated_users
    for u in updated_users:
        
        # store the new user in users list
        users.append(u)

    # return the updated users 
    return updated_users


# function to get user by id
def get_user_by_id(id):
    return next((u for u in users if u['id'] == id), None)

# function to get last object and get value for key id
def get_last_user_id():
    return users[len(users)-1]['id'] 
