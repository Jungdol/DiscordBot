import discord
from discord.ext import commands
import datetime
import asyncio
import importlib
import load_json_variable as variable
import Timetable as ttb

prefix = "!"  # 명령어 맨 앞에 붙여야 실행됨
bot = commands.Bot(command_prefix=prefix)


class MainTime:  # 모든 곳에 쓰여야 하기에 class 화
    is_time_table_stop = False
    isReturn = False

    tn = datetime.datetime.now()
    st = tn.strftime("%H:%M:%S")
    dd = tn.strftime('%Y-%m-%d')
    ss = tn.strftime("%S")
    pass


morning_sends = "조례 줌 들어오세요\n링크 : 줌 링크"  # 조례할 때 출력할 문장
afternoon_sends = "종례 시간입니다. 밴드 종례 출석체크 해주세요."  # 종례할 때 출력할 문장


def men(message):  # 멘션 기능 (저희 학과 채널은 2-8, 2-9로 운영)
    secondGradeClass = discord.utils.get(message.guild.roles, name="2-9")
    return secondGradeClass


def days(is_return):  # days()는 실행 시의 요일
    day = datetime.datetime.now()
    if is_return:
        return day.strftime("%a")  # 함수 실행 후 매개변수가 True 일 시 요일 리턴 예 : 월요일이면 "Mon" 으로 리턴
    else:
        return None


def time_set():
    MainTime.tn = datetime.datetime.now()
    MainTime.st = MainTime.tn.strftime("%H:%M:%S")  # "시간:분:초"로 출력 예 : 22:00:01
    MainTime.ss = MainTime.tn.strftime("%S")  # 무분별한 업데이트를 막기 위한 초만 반환 -> 00 01 02 ...

    print(MainTime.st)  # 실행하면 시간:분:초 출력
    print(MainTime.ss)  # 초단위로 출력
    return MainTime.st  # 함수를 실행하면 시간:분:초 리턴


async def time_table_sends(ctx, day, period):
    # embed = discord.Embed(title="메인 제목", color=0x62c1cc)  # Embed 의 기본 틀(색상, 메인 제목, 설명)을 잡아줌

    subject = str(variable.json_data[day][period]["name"])  # Timetable.json 안의 요일, 교시 오브젝트 안 과목 이름
    teacher = str(variable.json_data[day][period]["teacher"])  # Timetable.json 안의 요일, 교시 오브젝트 안 선생님 이름
    how = str(variable.json_data[day][period]["how"])  # Timetable.json 안의 요일, 교시 오브젝트 안 온라인 진행방식 (Zoom, Google Meet)
    url = str(variable.json_data[day][period]["url"])  # Timetable.json 안의 요일, 교시 오브젝트 안 링크

    await sends(ctx, f'{men(ctx).mention} {subject} 5분뒤 {teacher} 선생님 수업입니다.\n{how}\n\n링크 : {url}')
    return None


async def sends(ctx, text):
    return await ctx.channel.send(text)  # ctx.channel.send("할 말")인데, 줄이기 위해서 함수화


async def time_check(ctx, time):
    async def sends_delay(type):
        if type == "time_table":
            await time_table_sends(ctx, days(True), str(period))  # 현재 요일, 교시를 time_table_sends 에 보내며 호출
        elif type == "morning_send":
            await sends(ctx, f'{men(ctx).mention} {morning_sends}')  # 종례 시간 일 시 공지
        elif type == "afternoon_send":
            await sends(ctx, f'{men(ctx).mention} {afternoon_sends}')  # 종례 시간 일 시 공지

        await asyncio.sleep(5)  # 중복 출력을 막기 위해 5초 딜레이

    if time == str(ttb.AM_TIME):  # 조례 시간일 시 공지
        await sends_delay("morning_send")

    for i in range(0, 6):  # 0~5까지 반복 총 6번 반복 -> 1~6교시 (월~목 7교시 금 6교시)
        if time == ttb.All_TIME(i):  # 만약 현재 시간이 모든 교시 시간과 같으면
            period = i + 1  # period 를 i+1로 넣은 후 (1~6교시인데, 0~5이기에 하나 더함)
            await sends_delay("time_table")  # 현재 요일, 교시를 embedSends 에 보내며 호출

        if (time == ttb.All_TIME(6)) and (days(True) != "Fri"):  # 금요일은 6교시이기 때문에 구분
            period = 7
            await sends_delay("time_table")

        if (time == ttb.PM_TIME("default")) and (days(True) != "Fri"):  # 위와 같이 금요일은 6교시라서 월~목 때 종례 알람
            await sends_delay("afternoon_send")  # 종례 시간 일 시 공지

        if (time == ttb.PM_TIME("friday")) and (days(True) == "Fri"):  # 금요일 종례 알람
            await sends_delay("afternoon_send")  # 종례 시간 일 시 공지


@bot.command(name="start")
async def time_table(ctx):
    is_one_min = False
    await ctx.channel.purge(limit=1)  # 명령어 실행한 메세지 삭제
    # 해당 명령어 시작 시 나오는 문구
    await sends(ctx, "시간표 공지 시작합니다.")
    MainTime.is_time_table_stop = True

    while True:
        if is_one_min:  # is OneMin == True
            await asyncio.sleep(60)  # 60초 딜레이 (1분)
            time_set()  # 60초마다 시간 업데이트 (1분)
            if MainTime.ss != "00":
                is_one_min = False

        elif not is_one_min:
            await asyncio.sleep(1)  # 1초 딜레이
            time_set()  # 1초마다 시간 업데이트
            if MainTime.ss == "00":  # 초가 00이면 (60초면)
                is_one_min = True

        await time_check(ctx, MainTime.st)

        if (MainTime.st == ttb.All_TIME(6)) and (str(days(True)) == "Fri"):  # 금요일 6교시 끝나고 5분 뒤 알람 종료
            await sends(ctx, "온라인 수업 공지 종료합니다.")
            return None  # 반복문을 빠져나가는 건 break 지만 함수 자체를 종료하는 상황에선 return 사용

        elif not MainTime.is_time_table_stop:  # stop 명령어를 사용 시 (is_time_table_stop == False) 반복문 빠져나감.
            return None

        if str(MainTime.st) == "00:00:00":  # 자정일 시 days 실행 (요일 업데이트)
            days(False)


@bot.event
async def on_ready():  # 봇이 처음 시작 시, 재로딩 시 시작
    days(False)
    time_set()
    # '시간표 공지' 라는 게임 중으로 설정합니다.
    game = discord.Game("시간표 공지")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("READY")


@bot.command(name="stop")  # stop 명령어 실행 시 is_time_table_stop = False 로 하여 시간 공지 멈춤 (반복문 break)
async def stop(ctx):
    MainTime.is_time_table_stop = False
    await sends(ctx, "시간표 공지를 취소했습니다.\ntime_table 변수 : " + str(MainTime.is_time_table_stop))
    return None


@bot.command(name="reload")
async def json_reload(ctx):
    await ctx.channel.send("시간표 리로드 중..")
    importlib.reload(variable)
    importlib.reload(ttb)
    await ctx.channel.send("시간표 리로드 완료")
    return None


@bot.command(name="confirm")
async def react_test(ctx, day):
    # 유저가 요청했던 채널로 전송합니다.
    for i in range(1, 8):
        await time_table_sends(ctx, day, str(i))
    return None


@bot.command(name="now")  # 현재 시간 출력
async def time_print(ctx):
    await ctx.channel.send(time_set())
    await ctx.channel.send(MainTime.st + " st 변수 출력")
    return None


bot.run("bot token")
