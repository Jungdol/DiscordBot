import discord
from discord.ext import commands
import datetime
import asyncio
import importlib
import excel_import as excel

prefix = "!"  # 명령어 맨 앞에 붙여야 실행됨
bot = commands.Bot(command_prefix=prefix)

day_period = list()


class MainTime:  # 모든 곳에 쓰여야 하기에 class 화
    is_time_table_stop = False
    isReturn = False

    tn = datetime.datetime.now()
    st = tn.strftime("%H:%M:%S")
    dd = tn.strftime('%Y-%m-%d')
    ss = tn.strftime("%S")
    pass


def men(message):  # 멘션 기능 (저희 학과 채널은 3-8, 3-9로 운영) @3-9
    return discord.utils.get(message.guild.roles, name="3-9")


async def sends(ctx, text):
    return await ctx.channel.send(text)  # ctx.channel.send("할 말")인데, 줄이기 위해서 함수화


def days(is_return):  # days()는 실행 시의 요일
    day = datetime.datetime.now()
    if is_return:
        return day.strftime("%a")  # 함수 실행 후 매개 변수가 True 일 시 요일 리턴 예 : 월요일이면 "Mon" 으로 리턴
    else:
        return None


def time_set():
    MainTime.tn = datetime.datetime.now()
    MainTime.st = MainTime.tn.strftime("%H:%M:%S")  # "시간:분:초"로 출력 예 : 22:00:01
    MainTime.ss = MainTime.tn.strftime("%S")  # 무분별한 업데이트를 막기 위한 초만 반환 -> 00 01 02 ...

    print(MainTime.st)  # 실행하면 시간:분:초 출력
    print(MainTime.ss)  # 초단위로 출력
    return MainTime.st  # 함수를 실행하면 시간:분:초 리턴


async def timetable_sends(ctx, day, period, max_period):
    # embed = discord.Embed(title="메인 제목", color=0x62c1cc)  # Embed 의 기본 틀(색상, 메인 제목, 설명)을 잡아줌

    timetable_list = excel.timetable(day, max_period)  # 시간표 과목 리스트
    subject_value_list = excel.subject(timetable_list[period - 1])  # 과목 실시간 수업 값 리스트

    subject = subject_value_list[0]  # subject.xlsx 안에 과목 이름
    teacher = subject_value_list[2]  # subject.xlsx 안에 선생님 이름
    platform = subject_value_list[1]  # subject.xlsx 안에 플랫폼 이름
    id = subject_value_list[3]  # subject.xlsx 안에 id
    password = subject_value_list[4]  # subject.xlsx 안에 password
    url = subject_value_list[5]  # subject.xlsx 안에 url 링크
    note = subject_value_list[6]  # subject.xlsx 안에 note

    timetable_message = f'{men(ctx).mention} {subject} 5분 뒤 {teacher} 선생님 수업입니다.\n플랫폼: {platform}\n회의 ID: {id} 비밀번호: {password}\n\n'

    if note != '':  # note가 비어있지 않을 때
        timetable_message = f'{men(ctx).mention} {subject} 5분 뒤 {teacher} 선생님 수업입니다.\n플랫폼: {platform}\n\n{note}\n\n'

    if url == '':  # url이 비어있을 때
        timetable_message += '링크는 없습니다.'
    else:
        timetable_message += f'링크 : {url}'
    await sends(ctx, timetable_message)
    return None


async def time_check(ctx, time):
    async def sends_delay(type, period=None):
        if type == "time_table":
            await timetable_sends(ctx, days(True), period, day_period)  # 현재 요일, 교시를 time_table_sends 에 보내며 호출
        elif type == "morning_send":
            await sends(ctx, f"{men(ctx).mention} {excel.setting('morning_send_message')}")  # 종례 시간 일 시 공지
        elif type == "afternoon_send":
            await sends(ctx, f"{men(ctx).mention} {excel.setting('afternoon_send_message')}")  # 종례 시간 일 시 공지

    if time == excel.day_timetable('start'):  # 조례 시간일 시 공지
        await sends_delay("morning_send")

    for i in range(0, day_period[1]):  # 현재 요일의 최대 교시까지 반복
        if time == excel.day_timetable('list')[i]:  # 만약 현재 시간이 모든 교시 시간과 같으면
            period = i + 1  # period 를 i+1로 넣은 후 (예시로 1~6교시인데, 0~5이기에 하나 더함)
            await sends_delay("time_table", period)  # 현재 요일, 교시를 embedSends 에 보내며 호출

    if time == excel.day_timetable('min_finish') and day_period[0] == 'minimum_period':  # 위와 같이 금요일은 6교시라서 월~목 때 종례 알람
        await sends_delay("afternoon_send")  # 종례 시간 일 시 공지

    elif time == excel.day_timetable('max_finish') and day_period[0] == 'maximum_period':  # 금요일 종례 알람
        await sends_delay("afternoon_send")  # 종례 시간 일 시 공지


@bot.command(name="start")
async def time_table(ctx):
    is_thirty_sec = False
    await ctx.channel.purge(limit=1)  # 명령어 실행한 메세지 삭제
    # 해당 명령어 시작 시 나오는 문구
    await sends(ctx, "시간표 공지 시작합니다.")
    MainTime.is_time_table_stop = True

    while True:
        if MainTime.ss == "00":  # 0초 일 때
            await asyncio.sleep(60)  # 60초 딜레이 (1분)
            time_set()  # 60초마다 시간 업데이트 (1분)
            is_thirty_sec = False  # 30초 딜레이 적용 안함

        elif MainTime.ss != "00":  # 0초가 아니면 (시간 어긋날 때)
            if not is_thirty_sec:  # 30초 딜레이가 적용 안됐을 때
                await asyncio.sleep(30)  # 30초 딜레이
                is_thirty_sec = True  # 30초 딜레이가 적용 됨
            else:  # 30초 딜레이 적용 후
                await asyncio.sleep(1)  # 1초 딜레이
            time_set()  # 시간 업데이트

        await time_check(ctx, MainTime.st)

        if MainTime.st == excel.setting('stop_notice_time') and days(True) == excel.setting('stop_notice_day'):
            # 공지 날짜와 시간에 종료
            await sends(ctx, "온라인 수업 공지 종료합니다.")
            return None  # 반복문을 빠져나가는 건 break 지만 함수 자체를 종료하는 상황에선 return 사용

        elif not MainTime.is_time_table_stop:  # stop 명령어를 사용 시 (is_time_table_stop == False) 반복문 빠져나감.
            return None

        if MainTime.st == "00:00:00":  # 자정일 시 days 실행 (요일 업데이트)
            day_period_setting()


def day_period_setting():
    days(False)

    for i in range(6):  # 월~금 5번  # 현재 요일이 최소 교시인지 최대 교시인지 체크
        if i <= len(excel.setting('minimum_period_day_list'))-1 and days(True) == excel.setting('minimum_period_day_list')[i]:  # 최소 교시일 때
            day_period.append('minimum_period')
            day_period.append(excel.setting('minimum_period'))
        elif i <= len(excel.setting('maximum_period_day_list'))-1 and days(True) == excel.setting('maximum_period_day_list')[i]:  # 최대 교시일 때
            day_period.append('maximum_period')
            day_period.append(excel.setting('maximum_period'))


@bot.event
async def on_ready():  # 봇이 처음 시작 시, 재로딩 시 시작
    day_period_setting()
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


@bot.command(name="confirm")
async def days_timetable(ctx, day):
    # confirm Mon --> 월요일 모든 시간표 출력
    test_period = 0

    for i in range(6):  # 호출하는 요일이 최소 교시인지 최대 교시인지 확인
        if i <= len(excel.setting('minimum_period_day_list'))-1 and day == excel.setting('minimum_period_day_list')[i]:
            test_period = excel.setting('minimum_period')
        elif i <= len(excel.setting('maximum_period_day_list'))-1 and day == excel.setting('maximum_period_day_list')[i]:
            test_period = excel.setting('maximum_period')

    for j in range(1, 8):  # 1교시~7교시
        await timetable_sends(ctx, day, j, test_period)
    return None


@bot.command(name="info")
async def info(ctx):
    # 봇 세팅 값 출력
    min_period = excel.setting('minimum_period')
    max_period = excel.setting('maximum_period')
    await sends(ctx, f"최소 교시: {min_period}\n최대 교시: {max_period}\n"
                     f"{min_period}교시 수업: {excel.setting('minimum_period_day_list')}\n"
                     f"{max_period}교시 수업: {excel.setting('maximum_period_day_list')}\n"
                     f"공지 종료 요일: {excel.setting('stop_notice_day')}\n공지 종료 시각: {excel.setting('stop_notice_time')}\n"
                     f"조례 시 보낼 메시지: {excel.setting('morning_send_message')}\n"
                     f"종례 시 보낼 메시지: {excel.setting('afternoon_send_message')}")


@bot.command(name="day_timetable")
async def day_timetable(ctx):
    day_timetable_sends = f"조회: {excel.day_timetable('start')}\n"

    for i in range(0, excel.setting('maximum_period')):
        day_timetable_sends += f"{i+1}교시: {excel.day_timetable('list')[i]}\n"

    day_timetable_sends += (f"{excel.setting('minimum_period')}교시 종례: {excel.day_timetable('min_finish')}\n"
                            f"{excel.setting('maximum_period')}교시 종례: {excel.day_timetable('max_finish')}")

    await sends(ctx, day_timetable_sends)


@bot.command(name="now")  # 현재 시간 출력
async def time_print(ctx):
    await sends(ctx, time_set())
    return None


bot.run(excel.setting('bot_token'))
