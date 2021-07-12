def AM_TIME():
    return "08:05:00"  # 조례 시간


# 해당 교시 1~6교시 까지
def All_TIME(i):
    period = ["08:25:00", "09:20:00", "10:15:00", "11:10:00", "13:15:00", "14:10:00", "15:05:00"]  # 1교시부터 7교시까지
    return period[i]


# 시간표 끝 (종례)
def PM_TIME(state):  # 종례 시간
    if state == "default":
        return "13:00:15"
    elif state == "friday":
        return "12:20:15"


# 공휴일, 재량휴업일
def PUBLIC_HOLIDAY(i):
    holiday = ["2021-05-03", "2021-05-04", "2021-05-05", "2021-05-19", "2021-05-28", "2021-09-20", "2021-09-21",
               "2021-09-22", "2021-11-30"]
    return holiday[i]
