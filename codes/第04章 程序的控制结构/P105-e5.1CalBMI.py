#e5.1CalBMI.py
height, weight = \
        eval(input("请输入身高(米)和体重(公斤)[逗号隔开]: "))
bmi = weight / pow(height, 2)
print("BMI 数值为：{:.2f}".format(bmi))
wto, dom = "", ""
if bmi < 18.5: # WTO 标准
	wto = "偏瘦"
elif bmi < 25: # 18.5 <= bmi < 25
	wto = "正常"
elif bmi < 30: # 25 <= bmi < 30
	wto = "偏胖"
else:
	wto = "肥胖"
if bmi < 18.5: # 我国卫生部标准
	dom = "偏瘦"
elif bmi < 24: # 18.5 <= bmi < 24
	dom = "正常"
elif bmi < 28: # 24 <= bmi < 28
	dom = "偏胖"
else:
	dom = "肥胖"
print("BMI 指标为:国际'{0}', 国内'{1}'".format(wto, dom))
