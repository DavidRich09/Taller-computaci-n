import json

def dicToJson(string):
    jsonData = json.loads(string)
    return jsonData


def JsonToString(jsonData):
    string = json.dumps(jsonData)
    return string


print(dicToJson('{ "name":"John", "age":30, "city":"New York"}'))
print(type((dicToJson('{ "name":"John", "age":30, "city":"New York"}'))))

print(JsonToString({'name': 'John', 'age': 30, 'city': 'New York'}))
print(type(JsonToString({'name': 'John', 'age': 30, 'city': 'New York'})))