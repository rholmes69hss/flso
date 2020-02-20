from collections import OrderedDict

def serialize_user(user):
    return OrderedDict([
        ("id",user.id),
        ("name", user.username)
    ])

def serialize_role(role):
    return OrderedDict([
        ("id",role.id),
        ("name", role.name)
    ])
