#e4.2TextProgressBar.py
import time
for i in range(101):
    print("\r{:2}%".format(i), end="")
    time.sleep(0.05)
