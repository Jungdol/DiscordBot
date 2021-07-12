import discord
from discord.ext import commands
import datetime
import asyncio
import load_json_variable as variable
import Timetable as ttb

prefix = "!"  # 명령어 맨 앞에 붙여야 실행됨
bot = commands.Bot(command_prefix=prefix)


class MyClass:  # 모든 곳에 쓰여야 하기에 class 화
    isTimetableStop = False
    isReturn = False

    tn = datetime.datetime.now()
    st = tn.strftime("%H:%M:%S")
    dd = tn.strftime('%Y-%m-%d')
    ss = tn.strftime("%S")
    pass


def men(a):  # 멘션 기능 (저희 학과 채널은 2-8, 2-9로 운영)
    secondGradeClassSix = discord.utils.get(a.guild.roles, name="2-9")
    return secondGradeClassSix


def days(isReturn):  # days()는 실행 시의 요일
    day = datetime.datetime.now()
    if isReturn:
        return day.strftime("%a")  # 함수 실행 후 매개변수가 True 일 시 요일 리턴 예 : 월요일이면 "Mon" 으로 리턴
    else:
        return None


def timeSet():
    MyClass.tn = datetime.datetime.now()
    MyClass.st = MyClass.tn.strftime("%H:%M:%S")  # "시간:분:초"로 출력 예 : 22:00:01
    MyClass.ss = MyClass.tn.strftime("%S")  # 무분별한 업데이트를 막기 위한 초만 반환 -> 00 01 02 ...

    print(MyClass.st)  # 실행하면 시간:분:초 출력
    print(MyClass.ss)  # 초단위로 출력
    return MyClass.st  # 함수를 실행하면 시간:분:초 리턴


async def embedSends(a, day, period):
    embed = discord.Embed(title="메인 제목", color=0x62c1cc)  # Embed 의 기본 틀(색상, 메인 제목, 설명)을 잡아줌

    subject = str(variable.json_data[day][period]["name"])  # Timetable.json 안의 요일, 교시 오브젝트 안 과목 이름
    teacher = str(variable.json_data[day][period]["teacher"])  # Timetable.json 안의 요일, 교시 오브젝트 안 선생님 이름
    # how = str(variable.json_data[day][period]["how"])  # Timetable.json 안의 요일, 교시 오브젝트 안 온라인 진행방식 (Zoom, Google Meet)
    url = str(variable.json_data[day][period]["url"])  # Timetable.json 안의 요일, 교시 오브젝트 안 링크

    await sends(a, "{} ".format(men(a).mention) + str(subject) + " 5분뒤 " + str(teacher) + " 선생님 수업입니다.\n링크 : " + url)
    return None


async def sends(a, b):
    return await a.channel.send(b)  # ctx.channel.send("할 말")인데, 줄이기 위해서 함수화


async def timeCheck(a, time):
    if time == str(ttb.AM_TIME):  # 조례 시간일 시 공지
        await sends(a, str("{} 조례 줌 들어오세요\n링크 : 줌 링크".format(men(a).mention)))

    for i in range(0, 6):  # 0~5까지 반복 총 6번 반복 -> 1~6교시
        if time == ttb.All_TIME(i):  # 만약 현재 시간이 모든 교시 시간과 같으면
            period = i + 1  # period 를 i+1로 넣은 후 (1~6교시인데, 0~5이기에 하나 더함)
            await embedSends(a, days(True), str(period))  # 현재 요일, 교시를 embedSends 에 보내며 호출
        if i == 6:
            if time == ttb.All_TIME(6):
                period = 7
                await embedSends(a, days(True), str(period))  # 현재 요일, 교시를 embedSends 에 보내며 호출

        if (time == ttb.All_TIME(6)) and (days(True) != "Fri"):  # 금요일은 6교시이기 때문에 and 사용
            period = 7
            await embedSends(a, days(True), str(period))

        if (time == ttb.PM_TIME("default")) and (days(True) != "Fri"):  # 위와 같이 금요일은 6교시라서 금요일은 종례 알람 꺼놓음
            await sends(a, str("{} 종례 시간입니다. 밴드 종례 출석체크 또는 줌 들어오세요.".format(men(a).mention)))  # 종례 시간 일 시 공지
        if (time == ttb.PM_TIME("friday")) and (days(True) == "Fri"):  # 금요일 종례 알람
            await sends(a, str("{} 종례 시간입니다. 밴드 종례 출석체크 또는 줌 들어오세요.".format(men(a).mention)))  # 종례 시간 일 시 공지


@bot.command(name="TimeStart")
async def Timetable(ctx):
    isOneMin = False
    await ctx.channel.purge(limit=1)  # 명령어 실행한 메세지 삭제
    # 해당 명령어 시작 시 나오는 문구
    await sends(ctx, "시간표 공지 시작합니다.")
    MyClass.isTimetableStop = True
    MyClass.isTimetableStop = True

    while True:
        if isOneMin:  # is OneMin == True
            await asyncio.sleep(60)  # 60초 딜레이 (1분)
            timeSet()  # 60초마다 시간 업데이트 (1분)
            if MyClass.ss != "00":
                isOneMin = False
        elif not isOneMin:
            await asyncio.sleep(1)  # 1초 딜레이
            timeSet()  # 1초마다 시간 업데이트
            if MyClass.ss == "00":  # 초가 00이면 (60초면)
                isOneMin = True

        await timeCheck(ctx, MyClass.st)
        if (MyClass.st == ttb.All_TIME(6)) and (str(days(True)) == "Fri"):  # 금요일 6교시 끝나고 5분 뒤 알람 종료
            await sends(ctx, "온라인 수업 공지 종료합니다.")
            break
        elif not MyClass.isTimetableStop:  # stop 명령어를 사용 시 (isTimeTableStop == False) 반복문 빠져나감.
            break
        if str(MyClass.st) == "00:00:00":  # 자정일 시 days 실행 (요일 업데이트)
            days(False)


@bot.event
async def on_ready():  # 봇이 처음 시작 시, 재로딩 시 시작
    days(False)
    timeSet()
    # '시간표 공지' 라는 게임 중으로 설정합니다.
    game = discord.Game("시간표 공지")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("READY")

    
@bot.command(name="TimeStop")  # stop 명령어 실행 시 isTimetableStop = False 로 하여 시간 공지 멈춤 (반복문 break)
async def stop(ctx):
    MyClass.isTimetableStop = False
    await sends(ctx, "시간표 공지를 취소했습니다.\nTimetable : " + str(MyClass.isTimetableStop))


@bot.command(name="timeNow")  # 현재 시간 출력
async def TimePrint(ctx):
    await ctx.channel.send(timeSet())
    await ctx.channel.send(MyClass.st+" st 변수 출력")
    return None


bot.run("봇 토큰")
