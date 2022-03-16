디스코드 봇이 V3으로 업데이트 되었습니다!<br>
변경사항은 다음과 같습니다<br>

```
json 파일을 읽는 것을 가독성 있게 하기 위해 excel로 변경

봇 설정을 setting.xlsx로 가능하게 하여 프로그래밍을 모르는 사람도
쉽게 사용할 수 있음
```

```
json이 excel로 변경된 사항
timetable.xlsx - timetable 시트

python 이 excel로 변경된 사항
timetable.xlsx - day timetable 시트

python 기능이 excel로 새로 개발된 사항
setting.xlsx
```
# 사용 방법
모든 설정이 끝나면 main.py를 실행하신 후 봇이 추가된 디스코드 채널에<br>
!start 를 보내면 !start 를 보낸 메시지가 삭제되고 봇이 메시지를 보냅니다.<br>
![discord com_channels_718334799541960704_948659508819935252_953683235416731678](https://user-images.githubusercontent.com/61561973/158633511-324be13d-b327-439e-8a45-336af83e273c.png)
<br><br>
![image](https://user-images.githubusercontent.com/61561973/158635269-a6a7e582-6bec-46c0-8efc-a715df1cf8c3.png)<br>
공지하는 시간이 되면 자동으로 해당 요일, 교시에 있는 수업을 공지해줍니다.<br>

<br><br>
공지 봇이 작동 중에 엑셀 파일을 변경하면 변경한 파일을 다시 읽습니다.<br>
시간표 변동이 있어도 다음 공지 시간 전까지 수정하면 됩니다.<br>
이외의 여러가지 명령어가 있습니다.<br>

# 명령어

## !start
엑셀 파일 3개를 읽은 뒤 공지를 시작합니다.<br>
![discord com_channels_718334799541960704_948659508819935252_953683235416731678](https://user-images.githubusercontent.com/61561973/158633511-324be13d-b327-439e-8a45-336af83e273c.png)

## !stop
공지를 종료합니다.
![image](https://user-images.githubusercontent.com/61561973/158637615-4f690ea9-42e4-4050-97b7-bd2ef5d4a764.png)

## !confirm 요일
해당 요일의 시간표를 전부 보냅니다.<br>
요일 부분은 반드시 축약어를 사용하셔야 합니다.<br>
예: !confirm Mon<br>
![image](https://user-images.githubusercontent.com/61561973/158638432-5c07b433-a693-42f8-8b22-ec79bc906c5d.png)

## !info
setting.xlsx 값을 전부 보냅니다.<br>
엑셀 파일을 제대로 읽는 지 확인할 때 쓰입니다.<br>
![image](https://user-images.githubusercontent.com/61561973/158638770-eb258a16-f46f-4300-8ee5-647f04406062.png)

## !day_timetable
timetable.xlsx - day timetable 시트 값을 보냅니다.<br>
일과 시간표 입니다. 엑셀 파일을 제대로 읽는 지 확인할 때 쓰입니다.<br>
![image](https://user-images.githubusercontent.com/61561973/158639060-74961702-e9b7-4b3b-817f-c4b9a3180e13.png)
## !now
현재 시간을 보냅니다.<br>
![image](https://user-images.githubusercontent.com/61561973/158639239-2a5ed0e3-6cf6-4d77-a5be-3a1586234902.png)

# 초기 설정
## 봇 생성
https://jhoplin7259.tistory.com/91<br>
위 링크를 들어가 따라해주시면 됩니다.<br>
이후에 시간이 된다면 직접 블로그에 올리겠습니다.<br>
토큰은 엑셀 파일 중 setting.xlsx 에 넣으시면 됩니다.

## 멘션 설정

main.py에 들어가시면<br>
```
def men(message):  # 멘션 기능 (저희 학과 채널은 3-8, 3-9로 운영) @3-9
    return discord.utils.get(message.guild.roles, name="3-9")
```

이 부분을 찾아주셔야 합니다. 봇이 공지할 때 멘션하는 함수입니다.<br>
저 부분을 디스코드에 있는 역할로 바꾸시면 해당 멘션으로 호출합니다.<br>
보통 name 부분을 역할 이름 그대로 넣으시면 적용됩니다.<br>
아무래도 멘션 기능은 디스코드 api를 사용하기도 해서 엑셀로 변환하기 껄끄러웠습니다.<br>
이 부분만 프로그래밍 하시면 됩니다.<br>
이외에 @everyone, @here 등은 직접 찾아주세요
<br><br>
현재 학과 채널 역할<br>
![image](https://user-images.githubusercontent.com/61561973/158617760-9ecfddf4-482d-422c-9729-19cd3ccdea2e.png)

## 엑셀 파일
엑셀 파일은 총 3개 있습니다.
```
settings.xlsx
timetable.xlsx
subject.xlsx
```
파일명이 변경되서는 안되며 파일 안 양식은 지켜주셔야 합니다.<br>
양식은 두꺼운 테두리로 해놓았습니다.

### setting.xlsx
![image](https://user-images.githubusercontent.com/61561973/158622978-5f1ae047-1f92-4ecb-ade0-324b57ed4797.png)
<br><br>
```
최소 교시: 수업 교시가 적은 값 입니다. (예: 6교시)
최대 교시: 수업 교시가 많은 값 입니다. (예: 7교시)

필요성을 못느껴 개발하지는 않았지만 모든 요일 다 동일한 시간에 끝난다면
깃허브에 이슈를 보내주시면 개발해드리겠습니다.
```
```
최소 교시 요일: 수업 교시가 적은 때 요일입니다. (예: 금요일 6교시)
최대 교시 요일: 수업 교시가 많은 때 요일입니다. (예: 월, 화, 수, 목 7교시)
```
```
공지 중일 때 공지 종료 날짜가 된 후
공지 종료 시각이 되면 공지를 종료합니다.
```
```
조례, 종례 시 보낼 문장은 각각 조례, 종례 시간이 됐을 때 해당 문장을 보냅니다.
줄 바꿈이 필요하다면 엑셀에서 Alt+Enter을 누르면 줄 바꿈이 됩니다.
```
```
디스코드 봇 토큰은 디스코드 봇을 실행 할 시 필요한 것입니다.
암호라고 보면 편하며, 이것이 외부에 노출되면 악용될 수 있으니 조심해주세요.
```
### timetable.xlsx

#### timetable sheet
timetable 시트 입니다.<br>
![image](https://user-images.githubusercontent.com/61561973/158626837-3f44cca5-25c8-4f1b-9f8e-9e8ac2441014.png)
<br><br>
![image](https://user-images.githubusercontent.com/61561973/158627036-96ba56f8-176d-46a5-b062-e624dae0f080.png)
<br><br>
1행과 A열은 건드리시면 안됩니다. 데이터를 읽을 때 필요한 부분입니다.<br>
교시는 추가하거나 줄일 수 있으며 A열에 교시를 추가하거나 지우고 사용하시면 됩니다.<br>
대신 setting 값도 같이 바꾸셔야 합니다.<br>
아쉽게도 요일은 추가하거나 줄일 수 없습니다.<br>
과목을 시간표에 맞게 넣으시면 되며, **들어간 과목 이름이 공지할 때 사용합니다.**<br>
**여기에 들어간 과목 이름이 subject.xlsx 과목 이름과 같아야 합니다.**

#### day timetable sheet
day timetable 시트 입니다.<br>
![image](https://user-images.githubusercontent.com/61561973/158628306-9c9df17b-a10e-49d7-8115-bd6334d43a3e.png)
<br><br>
![image](https://user-images.githubusercontent.com/61561973/158628473-951f0966-57c3-41f8-8a3e-ed11d961cc1f.png)
<br><br>
Start time 쪽에는 공지하는 시간을 넣어주시면 됩니다.<br>
디스코드 봇이 공지할 때 메시지가 5분 뒤 라고 기본으로 적혀있습니다.<br>
그 부분은 직접 프로그래밍 하셔야 합니다.<br><br>
Start는 조례, Min Finish는 최소 교시 종례, Max Finish는 최대 교시 종례 시간입니다.<br>
공지할 교시는 더 추가할 수 있으며, Min Finish와 Max Finish 위쪽에 넣으셔야 됩니다.<br>
![image](https://user-images.githubusercontent.com/61561973/158630298-55202834-44dd-4199-a44f-c4992ff9cffe.png)<br>
단 공지할 교시를 추가할 때에는 셀 서식을 위 이미지로 설정하셔야 됩니다.<br>
note 쪽에는 단순한 설명입니다. 아무 기능도 없습니다.<br>

### subject.xlsx
![image](https://user-images.githubusercontent.com/61561973/158630571-6a2760b6-0891-48d1-9972-c1f529ea79c4.png)
<br><br>
```
name: 과목명
platform: 해당 과목의 온라인 수업 플랫폼
(예: Zoom, Whale On 등)
teacher: 선생님 성함
id: 해당 과목의 회의 ID
password: 해당 과목의 비밀번호
url: 해당 과목의 온라인 수업 링크
note: id, password가 없는 플랫폼일 때 사용(예: Google Meet 등)
```
엑셀 파일 오른쪽에 출력 예시가 있습니다.<br>
![image](https://user-images.githubusercontent.com/61561973/158632001-a5e78496-d640-48d6-a2d1-9ad22fd4f5bd.png)
<br><br>
이렇게 진행하시면 모든 초기 설정이 끝납니다.

