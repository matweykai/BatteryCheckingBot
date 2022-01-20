import psutil       # Checking battery status
import time         # sleep mode
from win10toast import ToastNotifier   # Push-messages
import random
import json
from BotSettings import BotSettings


def main_loop():
    """It's an infinite loop where bot checks battery level from time to time"""
    notifier = ToastNotifier()
    while True:
        settings_obj = get_settings()
        battery_status = psutil.sensors_battery()
        if battery_status.percent <= settings_obj.battery_limit and not battery_status.power_plugged:
            notifier.show_toast(settings_obj.notification_name,
                                random.choice(settings_obj.phrases),
                                duration=settings_obj.showing_time,
                                icon_path=settings_obj.icon_path,
                                )
        time.sleep(settings_obj.pause_time)


def get_settings() -> BotSettings:
    """Loads settings from json object

    Open json file with name 'settings.json', deserializes it and then
    creates and feel BotSettings object
    """
    try:
        with open("settings.json", "r", encoding="utf-8") as settings_file:
            # Deserialized settings object
            des_obj = json.load(fp=settings_file)

            bot_settings = BotSettings()
            # It's made for safety, now we can give access only to public fields
            public_fields = [field_name for field_name in dir(bot_settings) if field_name[0] != '_']

            for field_name in des_obj:
                if field_name in public_fields:
                    try:
                        # Attempt to set attribute
                        bot_settings.__setattr__(field_name, des_obj[field_name])
                    except AttributeError:
                        continue
    except OSError:
        bot_settings = BotSettings()

    return bot_settings


if __name__ == '__main__':
    main_loop()
