import datetime

wait_people = 14000605
#wait_people = 1200202

#1시간에 100명씩 탑승
# 매일 09시 ~ 21시까지 배 운행
# 12시간 = 1200명 탑승
# 대기인원 // 1200 = 대기일수 
# 년 수 = 대기일수 // 일년 일 수(one_year_days)
one_year_days = 0 
for i in range(10, 0, -1):
    one_year_days += 2**i
print(one_year_days)

#남은 일수 = 대기일수 % 일년 일 수(one_year_days)


remaining_days = 1437
accumulated_days = 0
month = 0

for i in range(10, 0, -1):
    accumulated_days += 2 ** i
    month += 1
    if accumulated_days > remaining_days:
        break

print(month)

def timeOfCrossingByShip(wait_people):
    one_year_days = 0
    for i in range(1, 11):
        one_year_days += 2 ** i
    year = (wait_people // 1200) // one_year_days
    rest_days = (wait_people // 1200) % one_year_days
    month = 0
    for i in range(10, 0, -1):
        month += 1
        if rest_days < 2 ** i :
            break
        rest_days -= 2 ** i
    day = rest_days
    hour = (wait_people % 1200) / 100 + 9
    minute_list = [25, 40, 55, 70, 85, 100]
    final_rest_people = wait_people % 1200
    hour = final_rest_people // 100 + 9

    start_min = [25, 40, 55, 70, 85, 100]
    rest_people = final_rest_people % 100 + 1

    today = datetime.datetime.today()

    for i in start_min:
        if i > rest_people:
            min = start_min.index(i) * 10 
            break
    
    if final_rest_people % 100 == 99:
        hour += 1
        min = 0
    if (today.minute + min) > 60:
        min = (today.minute + min) - 60
        hour += 1

    return f'{year}년 {month}월 {day}일 {hour:0>2}:{min:0>2} 출발'


print(timeOfCrossingByShip(wait_people))