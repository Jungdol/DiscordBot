질문 안받습니다. 꼭 구글링해서 찾아주세요.<br>
그리고 디스코드 봇 추가하는 방법도 구글링해서 찾아주세요.
<br><br>
**Discord API가 업데이트 되면서 오류가 발생했습니다.**
<br><br>
처음 실행하기 전 jsonSetting 폴더에 들어가 readMe.txt를 읽어보시고 Timetable.json을 생성한 후<br>
이 메모장이 있는 폴더 내에 json 파일을 옮겨주세요.
<br><br>
이후 Timetable.py 부분에 들어가 def 어쩌구 안 return 부분의 쌍따옴표 안에 있는 시간을 바꿔주세요.
<br><br>
그리고 아래 보시면 중간, 기말고사 날짜도 있는데 date = {} 안에 있는 날짜를 변경해주세요.<br>
꼭 형식에 맞게 넣어주세요. 예 : date = {"2021-04-26", "2021-04-27", "2021-04-28"}<br>
yyyy-mm-dd 형식<br>
만약 중간, 기말이 없으면 영원히 안 올 시간대로 따옴표 부분만 바꿔주세요.<br>
date = {"2099-12-29", "2099-12-30", "2099-12-31"}
<br><br>
코딩 좀 다룰 줄 아는 분들은<br>
DiscordBot.py 내에<br>
def examCheck(a): ... 생략<br>
아래쪽에 보면 for문 있는데<br>
for i in range(0, 2):  # 지금 날짜가 1, 2학기 중간고시, 기말고시 인지 확인<br>
for문 부분을 싹 지워주시면 됩니다.
<br><br>
저장 한 후
<br><br>
DiscordBot.py에 들어가시면<br>
def men(a): ... 생략<br>
이 부분이 보일텐데 이 부분은 멘션하는 함수입니다.<br>
저 부분을 재량껏 바꾸시면 해당 멘션으로 호출합니다.<br>
구글링해서 찾은 후 수정하세요.
<br><br>
 스크롤을 조금만 하시면
@bot.command(name="TimeStart")<br>
def timeCheck(a): ... 생략<br>
부분이 보일겁니다. 그 안의 부분만 수정하시면 됩니다.<br>
최대한 모든 부분에 주석처리를 해놓았으니 그걸 보시고 수정하시면 됩니다.<br>
또한 현재 파일은 월~목은 1~7교시, 금요일은 1~6교시까지 인데 이건 직접 수정하셔야 돼요.<br>
주석을 충분히 많이 해놓았으니 충분히 수정하실 수 있을 겁니다.<br>
<br>
스크롤을 좀 내려서<br>
@bot.command(name="TimeStart")<br>
async def Timetable(ctx): ... 생략
<br><br>
부분에
<br><br>
timeCheck(ctx)<br>
        if (MyClass.st == str(ttb.SEVENTH_TIME)) and str(days(True)) == "Fri":  # 금요일 6교시 끝나고 5분 뒤 알람 종료<br>
            await sends(ctx, "온라인 수업 공지 종료합니다.")<br>
            break<br>
        elif not MyClass.isTimetableStop:  # stop 명령어를 사용 시 (isTimeTableStop == False) 반복문 빠져나감.<br>
            break<br>
        if str(MyClass.st) == "00:00:00":  # 자정일 시 days 실행 (요일 업데이트)<br>
            days(False)<br>

이렇게 되어 있는 부분은 파이썬을 이해하신다면 break 때문입니다.<br>
이 부분에 금요일 6교시 공지 종료하는 부분과 반복문 종료가 있는데 재량껏 바꿔주세요.<br>
실행 명령어는 !TimeStart, 종료는 !stop 입니다.
