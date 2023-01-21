import requests, json, pprint
url='https://api.tvmaze.com/singlesearch/shows?q=girls'
params={"q":"star trek"}

response=requests.get(url,params)

if response.status_code == 200:
    #o/p in text
    #print(type(response.text))
    #o/p in dictonary
    data=json.loads(response.text)
    #pprint.pprint(data)
    name= data['name']
    premiered= data['premiered']
    summary= data['summary']
    print(f"{name} premiered on {premiered}.")
    print(summary)
    print(data['image']['medium'])
else:
    print(f"Error: {response.status_code}")