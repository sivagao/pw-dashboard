import json, requests, time

person_url = 'http://who.wandoulabs.com/api/v1/list/person'
cookies = {
    'user': '"eyJlbWFpbCI6ICJnYW9oYWlsYW5nQHdhbmRvdWppYS5jb20ifQ==|1398245626|1c68c3b6e4d397dd4b0d630993efe029e6aeab02"'
}

# with open('./admin/fixture/person.json') as json_data:
#     person_data = json.load(json_data)
#     person_dict = dict(zip(map(lambda x:x["id"], person_data), person_data))

time_lastfetch = 0
person_dict = {}
def get_person_dict():
    global time_lastfetch
    global person_dict
    if (time.time()-time_lastfetch) > 400:
        time_lastfetch = time.time()
        person_data = requests.get(person_url, cookies=cookies).json()
        person_dict = dict(zip(map(lambda x:x["id"], person_data), person_data))
    return person_dict

def getPersonImg(id):
    return get_person_dict().get(id, {}).get('img', 'http://img.wdjimg.com/who/avatar0.png')
