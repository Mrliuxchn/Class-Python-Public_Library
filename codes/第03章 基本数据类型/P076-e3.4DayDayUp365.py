dayup, dayfactor = 1.0, 0.01
for i in range(365):
    if i % 7 not in [6, 0]:
        dayup = dayup * (1 + dayfactor)
    else:
        dayup = dayup * (1 - dayfactor)
print("向上5 天向下2 天的力量: {:.2f}.".format(dayup))
