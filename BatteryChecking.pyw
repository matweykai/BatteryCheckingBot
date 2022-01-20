import psutil       # Checking battery status
import time         # sleep mode
from win10toast import ToastNotifier   # Push-messages
import random
import json


def main_loop():
    notifier = ToastNotifier()
    while True:
        settings_obj = get_settings()
        battery_status = psutil.sensors_battery()
        if battery_status.percent <= settings_obj['battery_limit'] and not battery_status.power_plugged:
            notifier.show_toast(settings_obj['notification_name'],
                                random.choice(settings_obj['phrases']),
                                duration=settings_obj['showing_time'],
                                icon_path=settings_obj['icon_path'],
                                )
        time.sleep(settings_obj['pause_time'])


def get_settings() -> dict:
    with open("settings.json", "r") as settings_file:
        # Deserialized settings object
        des_obj = json.load(fp=settings_file)

        result_dictionary = {
            "phrases": ["Battery charge is running out"],
            "notification_name": "Battery notification",
            "battery_limit": 100,
            "pause_time": 5,
            "showing_time": 3,
            "icon_path": "",
        }

        for field in des_obj:
            if field in result_dictionary.keys():
                result_dictionary[field] = des_obj[field]

        return result_dictionary


if __name__ == 'main':
    main_loop()
