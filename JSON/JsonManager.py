import json

def dicToJson(string):
    jsonData = json.loads(string)
    return jsonData

def JsonToString(jsonData):
    string = json.dumps(jsonData)
    return string

jsonDataIn =dicToJson('{ "name":"John", "age":30, "city":"New York"}')
print(jsonDataIn)
print(jsonDataIn["city"])

print(type((dicToJson('{ "name":"John", "age":30, "city":"New York"}'))))

print(JsonToString({'name': 'John', 'age': 30, 'city': 'New York'}))
print(type(JsonToString({'name': 'John', 'age': 30, 'city': 'New York'})))
