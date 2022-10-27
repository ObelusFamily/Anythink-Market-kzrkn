# just call the api to populate it.
import requests
import json 
import random 

N = 101

for i in range(N):
    seed = random.randint(0,10000)
    user = {
        'user': {
        'username': "user"+str(seed),
        'email': f"user_{seed}@email.com",
        'password': "password",
        },
    }

    r = requests.post('http://localhost:3000/api/users',json=user)
    print(r.text)

    #reply = json.loads(r.json())
token = r.json()['user']['token']


for i in range(N):
    item = {
  "item": {
    "title": "title-"+str(seed)+"s-"+str(i),
    "description": "string",
    "body": "string",
    "image": "string",
    "tagList": []
  }
}

    r = requests.post('http://localhost:3000/api/items',json=item,headers={"Authorization":"Token "+token})
    print(r.text)



for i in range(N):
    comment = {
  "comment": {
    "body": "Hello world!"
  }
}
    slug = "title-"+str(seed)+"s-"+str(i)
    r = requests.post(f'http://localhost:3000/api/items/{slug}/comments',json=comment,headers={"Authorization":"Token "+token})
    print(r.text)

