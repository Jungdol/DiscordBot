import json


def get_token():
    with open('parameter.json', 'r') as file:
        json_data = json.load(file)

    file.close()
    return json_data['bot-token']


with open('Timetable.json', 'r', encoding="utf8") as f:
    contents = f.read()  # string 타입
    json_data = json.loads(contents)

f.close()
