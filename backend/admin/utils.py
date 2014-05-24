import json, requests, time

person_url = 'http://who.wandoulabs.com/api/v1/list/person'
cookies = {
    'user': '"eyJlbWFpbCI6ICJnYW9oYWlsYW5nQHdhbmRvdWppYS5jb20ifQ==|1400959170|764d57bc374ae60b073f6f42310c655c7eddf364"'
}

with open('./admin/fixture/person.json') as json_data:
    _person_data = json.load(json_data)
    _person_dict = dict(zip(map(lambda x:x["id"], _person_data), _person_data))

time_lastfetch = 0
person_dict = {}
def get_person_dict():
    global time_lastfetch
    global person_dict
    if (time.time()-time_lastfetch) > 400:
        time_lastfetch = time.time()
        print 'going to fetch api'
        try:
            person_data = requests.get(person_url, cookies=cookies).json()
            person_dict = dict(zip(map(lambda x:x["id"], person_data), person_data))
        except Exception as e:
            print 'fetch error, using local data'
            person_dict = _person_dict
    return person_dict

def getPersonImg(id):
    # print get_person_dict()
    return get_person_dict().get(id, {}).get('img', 'http://img.wdjimg.com/who/avatar0.png')
