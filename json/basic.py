import json, datetime

data = {
    'first_name': 'Eugene',
    'last_name': 'Petrov',
    'age': 35,
    'hobbies': [
        'guitar',
        'cars',
        'mountains',
        'adventures'
    ]
}

# convert dict to json string
json_data = json.dumps(data)
# print(json_data)

# write dict to json file
# with open('data/output.json', 'w') as f:
#     json.dump(data, f, indent=4)


# read data from json string
json_data = '{"first_name": "Eugene"}'
data = json.loads(json_data)
# print(data['first_name'])

# read data from json file
with open('data/output.json', 'r') as f:
    data = json.load(f)
    # print(data['hobbies'][2])


# problems with json
data = {
    'current_date': datetime.datetime.now()
}

# json_data = json.dumps(data)
# print(json_data)

# solving problem with hooks
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return {
                'value': obj.strftime('%d/%m/%Y %H:%M:%S'),
                '__datetime__': True
            }
        elif isinstance(obj, datetime.date):
            return {
                'value': obj.strftime('%d/%m/%Y'),
                '__date__': True
            }
        return json.JSONEncoder.default(self, obj)

data = {
    'first_name': 'Eugene',
    'last_name': 'Petrov',
    'birthday': datetime.date(1986, 9, 29),
    'hired_at': datetime.datetime(2006, 9, 29, 12, 30, 5),
    'hobbies': [
        'guitar',
        'cars',
        'mountains',
        'adventures'
    ]
}

# to string
json_data = json.dumps(data, cls=ComplexEncoder)
# print(json_data)

# to file
# with open('data/output2.json', 'w') as f:
#     json.dump(data, f, cls=ComplexEncoder, indent=4)

# get from file
def as_date_datetime(dct):
    # print(dct)
    if '__datetime__' in dct:
        return datetime.datetime.strptime(dct['value'], '%d/%m/%Y %H:%M:%S')
    if '__date__' in dct:
        return datetime.datetime.strptime(dct['value'], '%d/%m/%Y').date()
    return dct

with open('data/output2.json', 'r') as f:
    data = json.load(f, object_hook=as_date_datetime)
    print(data['hired_at'])
