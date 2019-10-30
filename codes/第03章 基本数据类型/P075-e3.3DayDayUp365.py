import math
dayfactor = 0.01
dayup = math.pow((1.0 + dayfactor), 365) # 每天提高0.01
daydown = math.pow((1.0 - dayfactor), 365) # 每天荒废0.01
print("向上: {:.2f}, 向下: {:.2f}.".format(dayup, daydown))
