import json

#### serializing to json
# users = [
#   {
#     "date_added": "2019-02-27T16:46:58.155Z",
#     "is_primary": False,
#     "username": "Devyn21",
#     "pp_email": "Carmelo54@yahoo.com",
#     "pp_password": "L7RY9fmECg0Krll"
#   },
#   {
#     "date_added": "2019-02-22T09:04:49.556Z",
#     "is_primary": False,
#     "username": "Hattie_Hoeger",
#     "pp_email": "Frances.Kohler@gmail.com",
#     "pp_password": "XRiD2NsGPJ1Hn3v"
#   },
#   {
#     "date_added": "2019-02-25T00:03:39.464Z",
#     "is_primary": False,
#     "username": "Verner_Thompson",
#     "pp_email": "Rigoberto95@hotmail.com",
#     "pp_password": "tInPbQbpf0LHDbm"
#   }
# ]

# with open('inout/data/users-in.json', 'w') as f:
#     json.dump(users, f, indent=2)


#### deserializing

# with open('inout/data/users.json', 'r') as f:
#     users = json.load(f)

# print(users)

class User(object):
    def __init__(self, date_added, is_primary, username, pp_email, pp_password):
        self.date_added = date_added
        self.is_primary = is_primary
        self.username = username
        self.pp_email = pp_email
        self.pp_password = pp_password

    def to_json(self):
        return { 'date_added': self.date_added,
                'is_primary': self.is_primary,
                'username': self.username,
                'pp_email': self.pp_email,
                'pp_password': self.pp_password
                }
    @classmethod
    def from_json(cls, obj):
        return cls(obj['date_added'],
            obj['is_primary'],
            obj['username'],
            obj['pp_email'],
            obj['pp_password']
            )

    def __repr__(self):
        return f'<User ({self.date_added}, {self.is_primary}, {self.username}, {self.pp_email}, {self.pp_password})'


with open('inout/data/users.json', 'r') as f:
    users = json.load(f, object_hook=User.from_json)

print(users)
