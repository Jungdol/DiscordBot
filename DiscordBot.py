import discord
from discord.ext import commands
from discord.utils import get
import datetime
import load_json_variable as variable
import Timetable as ttb
import os

prefix = "*"  # 명령어 맨 앞에 붙여야 실행됨
bot = commands.Bot(command_prefix=prefix)


def men(a):
    secondGradeClassSix = discord.utils.get(a.guild.roles, name="2-9")
    return secondGradeClassSix


def days():
    day = datetime.datetime.now()
    day.strftime("%a")
    return day


def timeSet():
    tn = datetime.datetime.now()
    st = tn.strftime("%H:%M:%S")

    print(st)
    return st


def changeDay():
    while True:
        timeSet()
        if timeSet() == "00:00:00":
            days()
            return None


async def embedSends(a, day, period):
    embed = discord.Embed(title="메인 제목", color=0x62c1cc)  # Embed 의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
    subject = str(variable.json_data[day][period]["name"])
    teacher = str(variable.json_data[day][period]["teacher"])
    how = str(variable.json_data[day][period]["how"])
    url = str(variable.json_data[day][period]["url"])

    await a.channel.send("{} ".format(men(ctx).mention) + subject + " " + teacher + " 선생님 수업입니다.\n기타 링크 : " + url)
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
    return None


async def sends(a, b):
    return await a.channel.send(b)


def changePeriod():
    while True:
        timeSet()
        if timeSet() == ttb.AM_TIME:
            return 1
        elif timeSet() == ttb.FIRST_TIME:
            return 2
        elif timeSet() == ttb.SECOND_TIME:
            return 3
        elif timeSet() == ttb.THIRD_TIME:
            return 4
        elif timeSet() == ttb.FOURTH_TIME:
            return 5
        elif timeSet() == ttb.FIFTH_TIME:
            return 6
        elif timeSet() == ttb.SIXTH_TIME:
            return 7
        elif timeSet() == ttb.SEVENTH_TIME:
            return 8
        elif timeSet() == ttb.PM_TIME:
            return 9


@bot.event
async def on_ready():
    days()
    timeSet()
    # '시간표 공지' 라는 게임 중으로 설정합니다.
    game = discord.Game("시간표 공지")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("READY")


@bot.event
async def on_message(message):
    # 봇이 메시지를 보낸 경우 어떠한 작업도 하지 않음.
    if message.author.bot:
        return None

    # Commands 이벤트 진행
    await bot.process_commands(message)


@bot.command(name="test")
async def react_test(ctx):
    # 유저가 요청했던 채널로 전송합니다.
    day = "Mon"
    period = "2"
    subject = str(variable.json_data[day][period]["name"])
    teacher = str(variable.json_data[day][period]["teacher"])
    how = str(variable.json_data[day][period]["how"])
    url = str(variable.json_data[day][period]["url"])
    # await embedSends("{}".format(men(ctx).mention)+ctx, day, period)
    await ctx.channel.send("{} ".format(men(ctx).mention) + subject + " " + teacher + " 선생님 수업입니다.\n기타 링크 : " + url)

    return None


@bot.command(name="TimetableStart")
async def Timetable(ctx):
    await sends(ctx, "시간표 공지 시작합니다. 봇 테스트 과정입니다. \n조례부터 종례까지 공지를 이 봇이 실행합니다. 만약 실행되지 않으면 오류이니 알려주시기 바랍니다.")
    changeDay()
    if changeDay() == 1:
        await ctx.channel.send("조례 줌 들어오세요\n링크 : https://zoom.us/j/2435254903?pwd=ZE5ldUpxK1lTYVErdFFMUkNOZnhDQT09")

    changePeriod()
    if changePeriod() == 1:
        period = "1"
        await embedSends(ctx, days(), period)
        changePeriod()
    elif changePeriod() == 2:
        period = "2"
        await embedSends(ctx, days(), period)
        changePeriod()
    elif changePeriod() == 3:
        period = "3"
        await embedSends(ctx, days(), period)
        changePeriod()
    elif changePeriod() == 4:
        period = "4"
        await embedSends(ctx, days(), period)
        changePeriod()
    elif changePeriod() == 5:
        period = "5"
        await embedSends(ctx, days(), period)
        changePeriod()
    elif changePeriod() == 6:
        period = "6"
        await embedSends(ctx, days(), period)
        changePeriod()
    elif changePeriod() == 7:
        period = "7"
        await embedSends(ctx, days(), period)
        changePeriod()
    elif days != "Fri" and changePeriod() == 8:
        period = "8"
        await embedSends(ctx, days(), period)
        changePeriod()
    elif days != "Fri" and changePeriod() == 9:
        await sends(ctx, "종례 시간입니다.\n밴드 종례 출석체크 해주세요")
    '''elif days == "Fri" and changePeriod() == 7:
        await sends(ctx, "종례 시간입니다.")'''
    return sends(ctx, "공지 종료")


@bot.command(name="시간")
async def TimePrint(ctx):
    await ctx.channel.send(timeSet())
    return None


access_token = os.environ["BOT_TOKEN"]

bot.run(access_token)
