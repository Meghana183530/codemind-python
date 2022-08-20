h,m=map(int,input().split(":"))

hour_angle = 0.5 * (h * 60 + m)
minute_angle = 6 * m
angle = abs(hour_angle - minute_angle)
angle = min(360 - angle, angle)
print(angle)
         