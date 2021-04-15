jsonSetting.py는 subject.py안의 함수들을 불러옵니다.

subject.py 내용부터 바꿔 주시구요
만약 Timetable.py의 해당 학교의 과목이 없으시면 만드시면 됩니다.
def 과목이름():
    return {"name": "과목 이름", "teacher": "담당 선생님", "how": "진행 방식 (Zoom, Google Meet)", "url": "Zoom, Google Meet 링크"}

이렇게 넣으시면 됩니다.

과목 세팅을 다 하시고 jsonSetting.py 로 넘어가 보면,

file_data... 내에 대괄호 부분만 바꾸시면 됩니다.
file_data["해당 요일"] = {"1": sbj.1교시 과목이름(), "2": sbj.2교시 과목이름(), "3": sbj.3교시 과목이름(), "4": sbj.4교시 과목이름(), "5": 5sbj.English(), "6": sbj.6교시 과목이름(), "7": sbj.7교시 과목이름()}
이렇게 세팅한 후 저장하시면 됩니다.

이후 jsonSetting.py를 실행하시면 이 파일이 들어있는 폴더 안에 Timetable.json이 생성됩니다.
DiscordBot.py와 같은 폴더에 있게 옮겨주세요.

만약 오류가 난다면


공통 : 철자, 대문자를 확인해주세요.

subeject.py
1.def 과목이름 할 때 소괄호를 넣었는 지, 소괄호 다음 콜론을 넣었는 지 확인해주세요. 예 : def 과목이름():

2. return 전에 들여쓰기가 되어 있는 지 확인해주세요. 예 :
def 과목이름():
    return {어쩌구}
파이썬은 들여쓰기로 구문을 확인합니다.
오류날까 불안하시면 그 파일 안 예제가 있는데 그거를 복붙하시고 과목 이름, 대괄호 부분만 수정하시면 됩니다.

2-1. return 부분에 쌍따옴표가 제대로 닫았는 지, 콜론은 잘 넣었는 지 예 : "name: "과목 이름"
대괄호는 제대로 닫았는 지 확인해 주세요.
3. 쉼표는 잘 넣었는 지 확인해 주세요. 예 : {"name": "과목 이름", "teacher": "담당 선생님" ... 생략 }

jsonSetting.py
1. import, print, with open 등등.. 부분들을 실수로 바꿨는 지 확인해주세요.

2. 중괄호는 제대로 닫았는 지, 대괄호, 쌍따옴표는 제대로 닫았는 지, 쉼표는 잘 넣었는 지 확인해주세요.
file_data["Mon"] = {"1": sbj.Literature(), ... 생략 }
