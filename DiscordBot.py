import discord
from discord.ext import commands
import datetime
import asyncio
import load_json_variable as variable
# import Timetable as ttb 원래는 Timetable.py를 불러올라 했으나 오류나서 class times 에 옮김.
import os

prefix = "*"  # 명령어 맨 앞에 붙여야 실행됨
bot = commands.Bot(command_prefix=prefix)


class MyClass:
    TimetableStop = False
    tn = datetime.datetime.now()
    st = tn.strftime("%H:%M:%S")
    pass


class times:
    AM_TIME = "08:05:00"  # 조례 시간
    # 시간표 시작
    FIRST_TIME = "08:25:00"
    SECOND_TIME = "09:20:00"
    THIRD_TIME = "10:15:00"
    FOURTH_TIME = "11:10:00"
    FIFTH_TIME = "13:15:00"
    SIXTH_TIME = "14:10:00"
    SEVENTH_TIME = "15:05:00"
    # 시간표 끝
    PM_TIME = "15:55:00"  # 종례 시간
    TEST_TIME = "00:26:30"
    pass


def men(a):
    secondGradeClassSix = discord.utils.get(a.guild.roles, name="2-9")
    return secondGradeClassSix


def days():  # days()는 실행 시의 요일
    day = datetime.datetime.now()
    return day.strftime("%a")  # 함수 실행시 실행 시의 요일 리턴 예 : 월요일이면 "Mon" 으로 리턴


def timeSet():
    MyClass.tn = datetime.datetime.now()
    MyClass.st = MyClass.tn.strftime("%H:%M:%S")  # "시간:분:초"로 출력 예 : 22:00:01

    print(MyClass.st)  # 실행하면 시간:분:초 출력
    return MyClass.st  # 함수를 실행하면 시간:분:초 리턴


async def embedSends(a, day, period):
    embed = discord.Embed(title="메인 제목", color=0x62c1cc)  # Embed 의 기본 틀(색상, 메인 제목, 설명)을 잡아줌
    subject = str(variable.json_data[day][period]["name"])
    teacher = str(variable.json_data[day][period]["teacher"])
    how = str(variable.json_data[day][period]["how"])
    url = str(variable.json_data[day][period]["url"])

    await a.channel.send(
        "{} ".format(men(a).mention) + " 5분뒤 " + subject + " " + teacher + " 선생님 수업입니다.\n기타 링크 : " + url)
    # await sends(a,"{}".format(men(ctx).mention)+subject+" "+teacher+" 선생님 수업입니다.\n기타 링크 : "+url)
    '''embed.add_field(name="과목", value=str(variable.json_data[day][period]["name"]), inline=False)
    embed.add_field(name="담당 선생님", value=str(variable.json_data[day][period]["teacher"]), inline=False)
    embed.add_field(name="수업 방법", value=str(variable.json_data[day][period]["how"]), inline=False)
    embed.add_field(name="기타 링크", value=str(variable.json_data[day][period]["url"]), inline=False)'''
    '''embed.add_field(name="과목", value=subject, inline=False)
    embed.add_field(name="담당 선생님", value=teacher, inline=False)
    embed.add_field(name="수업 방법", value=how, inline=False)
    embed.add_field(name="기타 링크", value=url, inline=False)
    embed.set_footer(text="Google Meet 링크는 변경되기에 없습니다.")
    await a.channel.send(embed=embed)  # embed 를 포함 한 채로 메시지를 전송합니다.'''
    # 주석 부분은 embed 오류나서 감싸놈. 변경방법 아시면 주석 푸시고 쓰셈
    return None


async def sends(a, b):
    return await a.channel.send(b)  # ctx.channel.send("할 말")인데, 줄이기 위해서 함수화


@bot.event
async def on_ready():
    days()
    timeSet()
    # '시간표 공지' 라는 게임 중으로 설정합니다.
    game = discord.Game("시간표 공지")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("READY")


@bot.command(name="test")
async def react_test(ctx):
    # 유저가 요청했던 채널로 전송합니다.
    '''day = "Mon"
    period = "2"
    subject = str(variable.json_data[day][period]["name"])
    teacher = str(variable.json_data[day][period]["teacher"])
    how = str(variable.json_data[day][period]["how"])
    url = str(variable.json_data[day][period]["url"])
    # await embedSends("{}".format(men(ctx).mention)+ctx, day, period)
    await ctx.channel.send("{} ".format(men(ctx).mention) + subject + " " + teacher + " 선생님 수업입니다.\n기타 링크 : " + url)
    ''' # 이 주석또한 embed 오류임. 테스트용
    b = "22:22:00"
    await sends(ctx, b + "로 알람 설정되었습니다.")
    a = True
    while a:
        await asyncio.sleep(1)
        timeSet()
        if str(MyClass.st) == b:
            await sends(ctx, "지정된 시간이 되었습니다.")
            a = False

    # return None


@bot.command(name="stop")
async def stop(ctx):
    MyClass.TimetableStop = False
    await sends(ctx, "시간표 공지를 취소했습니다.\nTimetable : " + str(MyClass.TimetableStop))


@bot.command(name="TimeStart")
async def Timetable(ctx):
    await sends(ctx, "시간표 공지 시작합니다. 봇 테스트 과정입니다. \n조례부터 종례까지 공지를 이 봇이 실행합니다. 만약 실행되지 않으면 오류이니 알려주시기 바랍니다.")
    MyClass.TimetableStop = True
    while True:
        await asyncio.sleep(1)
        timeSet()
        if MyClass.st == "22:04:00":
            print("시간 측정")
        if MyClass.st == str(times.AM_TIME):
            await ctx.channel.send("조례 줌 들어오세요\n링크 : https://zoom.us/j/2435254903?pwd=ZE5ldUpxK1lTYVErdFFMUkNOZnhDQT09")
        if MyClass.st == str(times.FIRST_TIME):
            period = "1"
            await embedSends(ctx, days(), period)  # days()는 실행 시의 요일, period 는 교시
        if MyClass.st == str(times.SECOND_TIME):
            period = "2"
            await embedSends(ctx, days(), period)
        if MyClass.st == str(times.THIRD_TIME):
            period = "3"
            await embedSends(ctx, days(), period)
        if MyClass.st == str(times.FOURTH_TIME):
            period = "4"
            await embedSends(ctx, days(), period)
        if MyClass.st == str(times.FIFTH_TIME):
            period = "5"
            await embedSends(ctx, days(), period)
        if MyClass.st == str(times.SIXTH_TIME):
            period = "6"
            await embedSends(ctx, days(), period)
        if MyClass.st == str(times.SEVENTH_TIME) and str(days()) != "Fri":
            period = "7"
            await embedSends(ctx, days(), period)
        if MyClass.st == str(times.PM_TIME) and str(days()) != "Fri":
            await sends(ctx, "종례 시간입니다.\n밴드 종례 출석체크 해주세요")
        if MyClass.st == str(times.SEVENTH_TIME) and str(days()) == "Fri":
            await sends(ctx, "온라인 수업 공지 종료합니다.")
            break
        elif not MyClass.TimetableStop:
            break
        if str(MyClass.st) == "00:00:00":
            days()


@bot.command(name="현재 시간")
async def TimePrint(ctx):
    await ctx.channel.send(timeSet())
    return None


bot.run("봇 토큰")
