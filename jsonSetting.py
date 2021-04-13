import json
from collections import OrderedDict
import subject as sbj  # subject.py 가져오기

file_data = OrderedDict()

# 시간표를 json 에 작성
file_data["Mon"] = {"1": sbj.Literature(), "2": sbj.Japanese(), "3": sbj.ApplicationProgramming(), "4": sbj.ApplicationProgramming(), "5": sbj.English(), "6": sbj.GameProgramming(), "7": sbj.GameProgramming()}
file_data["Tue"] = {"1": sbj.SmartCultureAppContentsProduction(), "2": sbj.SmartCultureAppContentsProduction(), "3": sbj.KoreanHistory(), "4": sbj.English(), "5": sbj.Autonomy(), "6": sbj.SmartCultureAppContentsProduction2(), "7": sbj.Exercise()}
file_data["Wed"] = {"1": sbj.Math(), "2": sbj.Social(), "3": sbj.ApplicationProgramming(), "4": sbj.ApplicationProgramming(), "5": sbj.English(), "6": sbj.Literature(), "7": sbj.KoreanHistory()}
file_data["Thu"] = {"1": sbj.ApplicationProgramming(), "2": sbj.ApplicationProgramming(), "3": sbj.English(), "4": sbj.CareerAndJob(), "5": sbj.Japanese(), "6": sbj.GameProgramming(), "7": sbj.GameProgramming()}
file_data["Fri"] = {"1": sbj.Exercise(), "2": sbj.Math(), "3": sbj.Science(), "4": sbj.KoreanHistory(), "5": sbj.CreativeActivities(), "6": sbj.CreativeActivities()}

# Print JSON
print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

with open('Timetable.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")