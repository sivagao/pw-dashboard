import json

json_data=open('./admin/fixture/person.json')
person_data = json.load(json_data)
person_dict = {}
for i in person_data:
    person_dict[i['id']] = i
json_data.close()

def getPersonImg(id):
    return person_dict[id].get('img', 'http://img.wdjimg.com/who/avatar0.png')
