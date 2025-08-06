# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Julie',
    'valid': True #changing this will either run or not run the message_friends function.
}

user2 = {
    'name': 'James',
    'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
        else:
            return print("Invalid user")
    return wrapper

@authenticated
def message_friends(user):
    print('Message has been sent')

message_friends(user1) # message has been sent
message_friends(user2) # Invalid user