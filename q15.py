"""
Q15: 対話型残業代自動算出システム
問題：「現在の時刻」「定時」「1時間あたりの残業代」を対話式に入力すると、
　　　　残業代が自動で表示されるシステムを作れ。
条件：時刻の入力は”17:00”のように入力される。
"""

current_time = input("現在の時刻（例：18:45）>")
regular_time = input("定時（例：17:00）>")
over_time = float(input("1時間あたりの残業代（円）>"))

ct_hour = float(current_time[0:2])
ct_min = float(current_time[3:5])
current_time_min = (ct_hour * 60) + ct_min #分単位にする

rt_hour = float(regular_time[0:2])
rt_min = float(regular_time[3:5])
regular_time_min = (rt_hour * 60) + rt_min #分単位にする

ot_h = round((current_time_min - regular_time_min)/60,2)
ot_pay = ot_h * over_time

print("残業時間は",ot_h,"時間です。")
print("残業代は",ot_pay,"円です。")