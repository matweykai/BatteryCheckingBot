import psutil       # Checking battery status
import time         # sleep mode
from win10toast import ToastNotifier   # Push-messages
import random
import json

phrases = ["Battery charge is running out"]
notification_name = "Battery notification"
battery_limit = 100
pause_time = 5
showing_time = 3
i_path = ""


def main_loop():
    notifier = ToastNotifier()
    while True:
        update_data()
        battery_status = psutil.sensors_battery()
        if battery_status.percent <= battery_limit and not battery_status.power_plugged:
            notifier.show_toast(notification_name, random.choice(phrases), duration=showing_time, icon_path=i_path)
        time.sleep(pause_time)


def update_data():
    file = open("settings.json", "r")
    des_obj = json.load(fp=file)
    for field in des_obj:
        if field in globals():
            globals()[field] = des_obj[field]
    file.close()


main_loop()
