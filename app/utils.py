from collections import OrderedDict

def serialize_user(user):
    return OrderedDict([
        ("id",user.id),
        ("name", user.username)
    ])
