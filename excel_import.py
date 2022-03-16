import pandas as pd
import openpyxl


def setting(type):  # 디스코드 봇 설정값
    settings_df = pd.read_excel('./settings.xlsx', sheet_name=0).fillna('')  # fillna 로 nan 값을 ''(None) 로 설정

    def null_remove(str_list):  # None 값을 리스트에서 없앰
        return list(filter(None, str_list))

    if type == 'minimum_period':  # 최소 교시(ex:6교시)
        return settings_df.iloc[0, 1]
    elif type == 'maximum_period':  # 최대 교시(ex:7교시)
        return settings_df.iloc[1, 1]

    elif type == 'minimum_period_day_list':  # 최소 교시를 하는 요일 (ex: 금요일 6교시)
        return null_remove(settings_df.iloc[2, 1:5].values.tolist())
    elif type == 'maximum_period_day_list':  # 최대 교시를 하는 요일 (ex: 월,화,수,목 7교시)
        return null_remove(settings_df.iloc[3, 1:5].values.tolist())

    elif type == 'stop_notice_day':  # 공지 종료 날짜 (ex:금요일)
        return settings_df.iloc[4, 1]
    elif type == 'stop_notice_time':  # 공지 종료 시각 (ex:오후 2시 45분)
        return settings_df.iloc[5, 1]

    elif type == 'morning_send_message':
        return settings_df.iloc[6, 1]
    elif type == 'afternoon_send_message':
        return settings_df.iloc[7, 1]

    elif type == 'bot_token':
        return settings_df.iloc[8, 1]


def timetable(day, max_period):  # 해당 요일의 시간표, 최대 교시 리스트로 반환
    timetable_sheet = pd.read_excel('./timetable.xlsx', sheet_name='timetable')
    return timetable_sheet.loc[:max_period - 1, day].values.tolist()


def day_timetable(type):  # 일과 시간표 반환
    day_timetable_sheet = pd.read_excel('./timetable.xlsx', sheet_name='day timetable')
    if type == 'start':
        return day_timetable_sheet.iloc[0, 1]
    elif type == 'list':
        return day_timetable_sheet.iloc[1:setting('maximum_period')+1, 1].values.tolist()
    elif type == 'min_finish':
        return day_timetable_sheet.loc[day_timetable_sheet['period'] == 'Min Finish', 'Start time'].values[0]
    elif type == 'max_finish':
        return day_timetable_sheet.loc[day_timetable_sheet['period'] == 'Max Finish', 'Start time'].values[0]


def subject(subject_name):
    subject_sheet = pd.read_excel('./subject.xlsx', sheet_name=0).fillna('')
    subject_list = subject_sheet.loc[subject_sheet.name == subject_name, 'name':'note'].values.tolist()

    for i in range(7):
        if type(subject_list[0][i]) == float:  # 간혹 password 가 전부 숫자일 경우 float형으로 소수점이 붙음. 때문에 int형으로 변환하여 소수점 제거.
            subject_list[0][i] = int(subject_list[0][i])

    return subject_list[0]
