import math
dayup = math.pow((1.0 + 0.005), 365) # 每天提高0.005
daydown = math.pow((1.0 - 0.005), 365) # 每天荒废0.005
print("向上: {:.2f}, 向下: {:.2f}.".format(dayup, daydown))
