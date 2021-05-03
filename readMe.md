질문 안받습니다. 꼭 구글링해서 찾아주세요.<br>
그리고 디스코드 봇 추가하는 방법도 구글링해서 찾아주세요.
<br><br>
**Discord API가 업데이트 되면서 가끔식 오류가 발생합니다.**<br>
**과도한 API를 불러온다는 것 같은데 정확한 오류를 찾으면 수정하겠습니다.**<
<br><br>
처음 실행하기 전 jsonSetting 폴더에 들어가 readMe.md를 읽어보시고 Timetable.json을 생성한 후<br>
이 메모장이 있는 폴더 내에 json 파일을 옮겨주세요.
<br><br>
이후 Timetable.py 부분에 들어가 def All_TIME period = 부분에 자신이 공지하고 싶은 시간으로 변경해주세요.<br>
저는 쉬는시간 5분 남을 때 공지합니다.<br>
```
def All_TIME(i):
    period = ["08:25:00", "09:20:00", "10:15:00", "11:10:00", "13:15:00", "14:10:00"]
    return period[i]
```
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
```
def men(a):  # 멘션 기능 (저희 학과 채널은 2-8, 2-9로 운영)
    secondGradeClassSix = discord.utils.get(a.guild.roles, name="2-9")
    return secondGradeClassSix
```

이 부분이 보일텐데 이 부분은 멘션하는 함수입니다.<br>
저 부분을 디스코드에 있는 역할로 바꾸시면 해당 멘션으로 호출합니다.<br>
구글링해서 찾은 후 수정해주세요.<br>
현재 저희 학과 채널 역할<br>
![image](https://user-images.githubusercontent.com/61561973/116888398-63722a00-ac66-11eb-91c9-91af1fc8e166.png)

<br><br>
 스크롤을 조금만 하시면
@bot.command(name="TimeStart")<br>
def timeCheck(a): ... 생략<br>
부분이 보일겁니다. 그 안의 부분만 수정하시면 됩니다.<br>
최대한 모든 부분에 주석처리를 해놓았으니 그걸 보시고 수정하시면 됩니다.<br>
또한 현재 파일은 월-목은 1-7교시, 금요일은 1-6교시까지 인데 이건 직접 수정하셔야 돼요.<br>
주석을 충분히 많이 해놓았으니 충분히 수정하실 수 있을 겁니다.<br>
<br>
스크롤을 좀 내려서<br>
@bot.command(name="TimeStart")<br>
async def Timetable(ctx): ... 생략
<br><br>
부분에
<br>
```
timeCheck(ctx)
        if (MyClass.st == str(ttb.SEVENTH_TIME)) and str(days(True)) == "Fri":  # 금요일 6교시 끝나고 5분 뒤 알람 종료
            await sends(ctx, "온라인 수업 공지 종료합니다.")
            break
        elif not MyClass.isTimetableStop:  # stop 명령어를 사용 시 (isTimeTableStop == False) 반복문 빠져나감.
            break
        if str(MyClass.st) == "00:00:00":  # 자정일 시 days 실행 (요일 업데이트)
            days(False)
```

이렇게 되어 있는 부분은 파이썬을 이해하신다면 break 때문입니다.<br>
이 부분에 금요일 6교시 공지 종료하는 부분과 반복문 종료가 있는데 재량껏 바꿔주세요.<br>
실행 명령어는 !TimeStart, 종료는 !stop 입니다.
