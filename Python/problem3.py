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