import json

with open('Timetable.json', 'r', encoding="utf8") as f:
    contents = f.read()  # string 타입
    json_data = json.loads(contents)

f.close()
