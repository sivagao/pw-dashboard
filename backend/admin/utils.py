import json

with open('./admin/fixture/person.json') as json_data:
    person_data = json.load(json_data)
    person_dict = dict(zip(map(lambda x:x["id"], person_data), person_data))

def getPersonImg(id):
    return person_dict[id].get('img', 'http://img.wdjimg.com/who/avatar0.png')
