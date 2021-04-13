def AM_TIME():
    return "08:05:00"  # 조례 시간


# 해당 교시 1~6교시 까지
def All_TIME(i):
    period = ["08:25:00", "09:20:00", "10:15:00", "11:10:00", "13:15:00", "14:10:00"]
    return period[i]


# 저희 학교가 금요일만 6교시라 7교시를 따로 함수 지정
def SEVENTH_TIME():
    return "15:05:00"


# 시간표 끝
def PM_TIME():  # 종례 시간
    return "15:55:00"


# 1학기 중간고사 날짜
def FIRST_MIDTERM_EXAMINATION(i):
    date = ["2021-04-26", "2021-04-27", "2021-04-28"]
    return date[i]


# 1학기 기말고사 날짜
def FIRST_FINAL_EXAMINATION(i):
    date = ["2021-07-05", "2021-07-06", "2021-07-07"]
    return date[i]


# 2학기 중간고사 날짜
def SECOND_MIDTERM_EXAMINATION(i):
    date = ["2021-10-11", "2021-10-12", "2021-10-13"]
    return date[i]


# 2학기 기말고사 날짜
def SECOND_FINAL_EXAMINATION(i):
    date = ["2021-12-15", "2021-12-16", "2021-12-17"]
    return date[i]


# 공휴일, 재량휴업일
def PUBLIC_HOLIDAY(i):
    holiday = ["2021-05-03", "2021-05-04", "2021-05-05", "2021-05-19", "2021-05-28", "2021-09-20", "2021-09-21",
               "2021-09-22", "2021-11-30"]
    return holiday[i]
